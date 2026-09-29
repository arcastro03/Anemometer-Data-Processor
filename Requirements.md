# IAP Sensor Data Processor – Requirements

## App Concept

The Sensor Data Processor is an application designed to process CSV data collected from pressure transducer sensors used for wind measurement. The sensors record differential pressure measurements that can be converted into wind velocity.
The application will allow a user to select a CSV file containing recorded sensor data and automatically calculate useful wind characteristics such as average wind speed and turbulence intensity. 
It will also provide plots that make it easier to visualize and compare sensor measurements.

---

# User Stories

## US-1: Import Sensor Data

**I want to select a CSV file containing sensor measurements so that I can analyze data from different experiments without modifying the program.**

### Acceptance Criteria
- The application allows the user to select a CSV file at runtime.
- The application successfully reads a correctly formatted CSV file.
- The application displays an error message if the selected file cannot be read.
- The application does not require the CSV file path to be hard-coded.

---

## US-2: Validate Sensor Data

**I want the application to validate the imported data so that invalid or incomplete measurements do not silently affect my results.**

### Acceptance Criteria
- The application checks that required columns are present before beginning analysis.
- Missing or non-numeric sensor values are detected.
- The application informs the user when invalid data is found.
- Invalid rows are either excluded from calculations or clearly reported to the user.

---

## US-3: Convert Pressure to Wind Velocity

**I want pressure measurements to be converted into wind velocity so that the raw pressure sensor data can be interpreted as wind speed.**

### Acceptance Criteria
- The application converts valid differential pressure measurements into wind velocity using the equation defined by the project.
- The application uses consistent units throughout the conversion.
- The resulting velocity values are associated with the correct samples or timestamps.
- The application does not modify the original input CSV.

---

## US-4: Calculate Average Wind Speed

**I want the application to calculate average wind speed so that I can quickly characterize the wind conditions during an experiment.**

### Acceptance Criteria
- The application calculates the arithmetic mean of the valid wind velocity samples.
- Invalid or excluded samples are not included in the average.
- The calculated average is displayed with its units.
- The result is reproducible when the same input file and settings are used.

---

## US-5: Calculate Turbulence Intensity

**I want the application to calculate turbulence intensity so that I can quantify how much the wind speed fluctuates during an experiment.**

### Acceptance Criteria
- The application calculates the standard deviation of the valid wind velocity measurements.
- Turbulence intensity is calculated using the project's defined turbulence-intensity equation.
- The application reports turbulence intensity as a percentage.
- The application identifies cases where turbulence intensity cannot be calculated, such as when the mean velocity is zero.

---

## US-6: Plot Wind Speed Data

**I want to plot wind velocity over the duration of the recording so that I can visually identify trends, fluctuations, and unusual measurements.**

### Acceptance Criteria
- The application produces a plot of wind velocity versus sample number or time.
- The graph contains labeled axes.
- The graph displays the units of wind velocity.
- The graph is generated from the same valid data used in the numerical analysis.

---

## US-7: Compare Multiple Sensor Channels

**I want the application to process multiple sensor channels from the same experiment so that I can compare wind measurements at different sensor locations.**

### Acceptance Criteria
- The application can identify multiple supported sensor columns in a CSV file.
- Statistics are calculated separately for each sensor channel.
- Each sensor is clearly identified in calculated results.
- Multiple sensor channels can be displayed on a plot without mixing their data.

---

## US-8: Export Processed Results

**I want to save processed results so that I can use them later in reports and further analysis.**

### Acceptance Criteria
- The user can export calculated results to a new file.
- The exported results identify the source sensor or channel.
- Average wind speed and turbulence intensity are included in the exported results.
- Exporting results does not overwrite the original sensor data unless the user explicitly chooses the same filename.

---

# Non-Functional Requirements

## NFR-1: Processing Performance

For a CSV file containing up to **100,000 data rows and 16 sensor channels**, the application shall complete data validation, wind-speed calculations, and summary-statistic calculations within **10 seconds** on the development computer.

This requirement can be tested by processing a known 100,000-row dataset and measuring execution time.

---

## NFR-2: Calculation Accuracy

For a test dataset with independently calculated reference values, the application's reported average wind speed and turbulence intensity shall differ from the reference calculations by no more than **0.1%**, excluding differences caused by explicitly documented rounding.

This requirement can be tested using a known dataset and reference calculations.

---

## NFR-3: Invalid Input Handling

For every tested CSV file that is missing one or more required columns, the application shall **stop analysis and display an error identifying the missing column or columns instead of terminating with an unhandled exception**.

This requirement can be tested using intentionally malformed CSV files.
