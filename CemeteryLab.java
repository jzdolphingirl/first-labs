import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.Objects;
import java.util.Scanner;
import java.util.TreeSet;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class CemeteryLab {
    private static final String DATA_FILE = "cemetery_orig.txt";
    private static final DateTimeFormatter DISPLAY_DATE = DateTimeFormatter.ofPattern("dd MMM yyyy", Locale.ENGLISH);
    private static final Pattern RESIDENT_PATTERN = Pattern.compile("^(.*?)(\\d{1,2}|xx)\\s+([A-Za-z]{3})\\s+(\\d{4})\\s+([^\\s]+)\\s+(.*)$");

    private static final List<Resident> RESIDENTS = new ArrayList<>();
    private static final TreeSet<String> STREET_NAMES = new TreeSet<>(String.CASE_INSENSITIVE_ORDER);

    public static void main(String[] args) {
        loadResidents();

        if (RESIDENTS.isEmpty()) {
            System.out.println("No cemetery records were loaded. Make sure cemetery_orig.txt is present in the project folder.");
            return;
        }

        try (Scanner scanner = new Scanner(System.in)) {
            menuLoop(scanner);
        }
    }

    private static void menuLoop(Scanner scanner) {
        while (true) {
            System.out.println();
            System.out.println("==== St Mary Magdalene Cemetery Database ====");
            System.out.println("1. Search by last name");
            System.out.println("2. Search by street name");
            System.out.println("3. Show street list");
            System.out.println("4. Sort by name");
            System.out.println("5. Sort by burial date");
            System.out.println("6. Sort by age at death");
            System.out.println("7. Sort by address");
            System.out.println("8. Show statistics");
            System.out.println("9. Show all residents");
            System.out.println("0. Exit");
            System.out.print("Select an option: ");

            String choice = scanner.nextLine().trim();

            switch (choice) {
                case "1":
                    System.out.print("Enter a last name: ");
                    String lastName = scanner.nextLine().trim();
                    printResults(findByLastName(lastName), "Residents with last name '" + lastName + "'");
                    break;
                case "2":
                    System.out.print("Enter a street name (or a partial match): ");
                    String street = scanner.nextLine().trim();
                    printResults(findByStreet(street), "Residents on street matching '" + street + "'");
                    break;
                case "3":
                    printStreetList();
                    break;
                case "4":
                    printResults(new ArrayList<>(RESIDENTS), "Residents sorted by name");
                    break;
                case "5":
                    printResults(sortByBurialDate(), "Residents sorted by burial date");
                    break;
                case "6":
                    printResults(sortByAge(), "Residents sorted by age at death");
                    break;
                case "7":
                    printResults(sortByAddress(), "Residents sorted by address");
                    break;
                case "8":
                    showStatistics();
                    break;
                case "9":
                    printResults(new ArrayList<>(RESIDENTS), "All residents");
                    break;
                case "0":
                    System.out.println("Goodbye.");
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
    }

    private static void loadResidents() {
        try (BufferedReader reader = new BufferedReader(new FileReader(DATA_FILE))) {
            String line;
            while ((line = reader.readLine()) != null) {
                String trimmed = line.trim();
                if (trimmed.isEmpty()) {
                    continue;
                }

                if (trimmed.startsWith("NAME") || trimmed.startsWith("----") || trimmed.startsWith("ST MARY")
                        || trimmed.startsWith("Burials") || trimmed.startsWith("Cemetery")
                        || trimmed.startsWith("Disclaimer") || trimmed.startsWith("grief")
                        || trimmed.startsWith("If you are sensitive") || trimmed.startsWith("Historic notes")) {
                    continue;
                }

                Resident resident = parseResident(trimmed);
                if (resident != null) {
                    RESIDENTS.add(resident);
                    STREET_NAMES.add(resident.coreStreet);
                }
            }
        } catch (IOException e) {
            System.out.println("Error reading " + DATA_FILE + ": " + e.getMessage());
        }
    }

    private static Resident parseResident(String line) {
        Matcher matcher = RESIDENT_PATTERN.matcher(line);
        if (!matcher.matches()) {
            return null;
        }

        String namePart = matcher.group(1).trim();
        String dayText = matcher.group(2);
        String monthText = matcher.group(3);
        String yearText = matcher.group(4);
        String ageText = matcher.group(5).trim();
        String addressText = matcher.group(6).trim();

        if (namePart.isEmpty() || yearText.isEmpty() || ageText.isEmpty() || addressText.isEmpty()) {
            return null;
        }

        String[] nameParts = namePart.split("\\s+");
        if (nameParts.length < 2) {
            return null;
        }

        String lastName = nameParts[nameParts.length - 1];
        String firstNames = namePart.substring(0, namePart.length() - lastName.length()).trim();

        Resident resident = new Resident();
        resident.fullName = namePart;
        resident.firstNames = firstNames;
        resident.lastName = lastName;
        resident.address = addressText;
        resident.coreStreet = normalizeStreet(addressText);
        resident.burialDate = parseBurialDate(dayText, monthText, yearText);
        resident.ageAtDeath = parseAge(ageText);
        return resident;
    }

    private static LocalDate parseBurialDate(String dayText, String monthText, String yearText) {
        int day = 1;
        try {
            if (!"xx".equalsIgnoreCase(dayText)) {
                day = Integer.parseInt(dayText);
            }
        } catch (NumberFormatException ignored) {
            day = 1;
        }

        int year;
        try {
            year = Integer.parseInt(yearText);
        } catch (NumberFormatException e) {
            year = 0;
        }

        int month = monthToNumber(monthText);
        try {
            return LocalDate.of(year, month, day);
        } catch (Exception e) {
            return LocalDate.of(year, 1, 1);
        }
    }

    private static int monthToNumber(String monthText) {
        switch (monthText.toLowerCase(Locale.ENGLISH)) {
            case "jan": return 1;
            case "feb": return 2;
            case "mar": return 3;
            case "apr": return 4;
            case "may": return 5;
            case "jun": return 6;
            case "jul": return 7;
            case "aug": return 8;
            case "sep": return 9;
            case "oct": return 10;
            case "nov": return 11;
            case "dec": return 12;
            default: return 1;
        }
    }

    private static double parseAge(String ageText) {
        String cleaned = ageText.trim();
        if (cleaned.isEmpty() || cleaned.equalsIgnoreCase("xx")) {
            return 0.0;
        }

        cleaned = cleaned.replaceAll("[,]", "");

        if (cleaned.matches("\\d+\\.?\\d*")) {
            return Double.parseDouble(cleaned);
        }

        String numberPart = cleaned.replaceAll("[^0-9.\\-]", "");
        if (numberPart.isEmpty()) {
            return 0.0;
        }

        double number = Double.parseDouble(numberPart);
        char unit = Character.toLowerCase(cleaned.charAt(cleaned.length() - 1));

        switch (unit) {
            case 'd':
                return number / 365.0;
            case 'w':
                return number / 52.0;
            case 'm':
                return number / 12.0;
            default:
                return number;
        }
    }

    private static String normalizeStreet(String address) {
        if (address == null || address.trim().isEmpty()) {
            return "Unknown";
        }

        String cleaned = address.trim();
        String candidate = cleaned;

        if (cleaned.contains(",")) {
            candidate = cleaned.substring(cleaned.lastIndexOf(',') + 1).trim();
        }

        if (candidate.isEmpty()) {
            candidate = cleaned;
        }

        candidate = candidate.replace("'", " ");
        String[] tokens = candidate.split("\\s+");
        StringBuilder builder = new StringBuilder();
        for (String token : tokens) {
            String normalizedToken = token.trim();
            if (normalizedToken.isEmpty()) {
                continue;
            }
            if (normalizedToken.matches("\\d+|\\d+/\\d+|\\d+\\.\\d+")) {
                continue;
            }
            if (normalizedToken.equalsIgnoreCase("mdx") || normalizedToken.equalsIgnoreCase("sry")
                    || normalizedToken.equalsIgnoreCase("ess") || normalizedToken.equalsIgnoreCase("kent")
                    || normalizedToken.equalsIgnoreCase("london")) {
                continue;
            }
            if (builder.length() > 0) {
                builder.append(" ");
            }
            builder.append(normalizedToken);
        }

        String result = builder.toString().trim();
        return result.isEmpty() ? candidate.trim() : result;
    }

    private static List<Resident> findByLastName(String lastName) {
        if (lastName == null || lastName.trim().isEmpty()) {
            return new ArrayList<>();
        }

        List<Resident> matches = new ArrayList<>();
        for (Resident resident : RESIDENTS) {
            if (resident.lastName.equalsIgnoreCase(lastName)) {
                matches.add(resident);
            }
        }
        matches.sort(Comparator.comparing((Resident r) -> r.fullName.toLowerCase(Locale.ENGLISH)));
        return matches;
    }

    private static List<Resident> findByStreet(String street) {
        if (street == null || street.trim().isEmpty()) {
            return new ArrayList<>();
        }

        List<Resident> matches = new ArrayList<>();
        String search = street.trim().toLowerCase(Locale.ENGLISH);
        for (Resident resident : RESIDENTS) {
            if (resident.coreStreet.toLowerCase(Locale.ENGLISH).contains(search)) {
                matches.add(resident);
            }
        }
        matches.sort(Comparator.comparing((Resident r) -> r.coreStreet.toLowerCase(Locale.ENGLISH))
                .thenComparing(r -> r.fullName.toLowerCase(Locale.ENGLISH)));
        return matches;
    }

    private static List<Resident> sortByBurialDate() {
        List<Resident> copy = new ArrayList<>(RESIDENTS);
        copy.sort(Comparator.comparing((Resident r) -> r.burialDate));
        return copy;
    }

    private static List<Resident> sortByAge() {
        List<Resident> copy = new ArrayList<>(RESIDENTS);
        copy.sort(Comparator.comparingDouble((Resident r) -> r.ageAtDeath).reversed());
        return copy;
    }

    private static List<Resident> sortByAddress() {
        List<Resident> copy = new ArrayList<>(RESIDENTS);
        copy.sort(Comparator.comparing((Resident r) -> r.coreStreet.toLowerCase(Locale.ENGLISH))
                .thenComparing(r -> r.fullName.toLowerCase(Locale.ENGLISH)));
        return copy;
    }

    private static void printResults(List<Resident> results, String title) {
        System.out.println();
        System.out.println(title);
        if (results == null || results.isEmpty()) {
            System.out.println("No matches found.");
            return;
        }

        for (Resident resident : results) {
            System.out.println(resident);
        }
    }

    private static void printStreetList() {
        System.out.println();
        System.out.println("Unique street names found in the cemetery database:");
        if (STREET_NAMES.isEmpty()) {
            System.out.println("No streets were loaded.");
            return;
        }

        int index = 1;
        for (String street : STREET_NAMES) {
            System.out.printf("%2d. %s%n", index++, street);
        }
    }

    private static void showStatistics() {
        if (RESIDENTS.isEmpty()) {
            System.out.println("No residents available.");
            return;
        }

        double totalAge = 0.0;
        double oldestAge = Double.NEGATIVE_INFINITY;
        Map<Integer, Integer> yearlyCounts = new HashMap<>();

        for (Resident resident : RESIDENTS) {
            totalAge += resident.ageAtDeath;
            oldestAge = Math.max(oldestAge, resident.ageAtDeath);
            int year = resident.burialDate.getYear();
            yearlyCounts.put(year, yearlyCounts.getOrDefault(year, 0) + 1);
        }

        double averageAge = totalAge / RESIDENTS.size();

        int highestYear = -1;
        int highestCount = -1;
        for (Map.Entry<Integer, Integer> entry : yearlyCounts.entrySet()) {
            if (entry.getValue() > highestCount) {
                highestCount = entry.getValue();
                highestYear = entry.getKey();
            }
        }

        System.out.println();
        System.out.println("=== Cemetery Statistics ===");
        System.out.printf("Average age at death: %.2f years%n", averageAge);
        System.out.printf("Oldest age at death: %.2f years%n", oldestAge);
        System.out.printf("Year with the highest mortality rate: %d (%d burials)%n", highestYear, highestCount);
    }

    private static class Resident {
        private String fullName;
        private String firstNames;
        private String lastName;
        private String address;
        private String coreStreet;
        private LocalDate burialDate;
        private double ageAtDeath;

        @Override
        public String toString() {
            return String.format("%s | Burial date: %s | Age: %.2f years | Address: %s | Street: %s",
                    fullName,
                    burialDate.format(DISPLAY_DATE),
                    ageAtDeath,
                    address,
                    coreStreet);
        }
    }
}





























































































