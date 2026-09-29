# AI Elicitation Audit

## Overview

I asked an AI tool to elicit requirements for my sensor data processing application. The AI produced several useful requirements, but reviewing its response showed that generated requirements cannot simply be accepted without checking whether they actually match the intended application. The response contained omissions, assumptions about features I had not requested, and non-functional requirements that were too vague to test.

---

# What the AI Missed

## 1. Handling Invalid Sensor Data

The largest omission was how the program should handle invalid or missing sensor measurements. Experimental sensor data may contain missing values, non-numeric values, or incomplete rows. The AI said that the program should report an error if a file cannot be opened, but it did not discuss what should happen if the file opens successfully but contains bad data.

I added a user story specifically requiring validation of the imported sensor data and defined what should happen when invalid values are detected.

## 2. Multiple Sensor Channels

My experiments can involve multiple pressure sensors rather than a single stream of measurements. The AI consistently referred to "sensor data" but never asked how many sensors may exist in one file or whether each sensor should be analyzed separately.

I added a requirement for identifying, processing, and comparing multiple sensor channels.

## 3. Required CSV Structure

The AI never asked what columns are required in the input CSV or how sensor channels and timestamps are identified. This is important because the program cannot reliably process an arbitrary CSV file without knowing its structure.

I added validation criteria requiring the application to check for required columns before performing calculations.

## 4. Zero Mean Velocity When Calculating Turbulence Intensity

The AI correctly suggested calculating turbulence intensity but did not consider the case where the average wind velocity is zero. Since turbulence intensity involves dividing by the mean velocity, this condition must be handled instead of producing an invalid result.

I added an acceptance criterion requiring the application to identify situations where turbulence intensity cannot be calculated.

## 5. Protecting the Original Experimental Data

The AI suggested importing and exporting data but did not state whether the original experimental CSV should be modified. Preserving raw experimental data is important, so I added requirements specifying that analysis should not modify the original input file.

---

# What the AI Invented

## 1. Saving Experiments Inside the Application

The AI added a complete feature for creating named experiments and reopening them later. I did not request an experiment database or project-management system. My intended application processes existing CSV files rather than maintaining its own collection of experiments.

Because this feature would significantly increase the scope of the project without helping the core data-processing goal, I did not include it in my requirements.

## 2. Zooming and Panning Graphs

The AI specified that users should be able to zoom and pan graphs. While this could be useful, I never requested interactive plotting. The initial version only needs to generate useful plots of the experimental data.

I therefore kept the plotting requirement but removed mandatory zoom and pan functionality.

## 3. PNG Graph Export

The AI required graphs to be exportable as PNG files. I had not specified an image-export requirement. This might be useful in a later version, but it is not currently necessary for the minimum application.

## 4. Cross-Platform Support

The AI suggested that the application work on Windows, macOS, and Linux. I never specified cross-platform compatibility. Requiring three operating systems would also create additional testing requirements that are unnecessary for the current project.

---

# What the AI Got Right

## 1. Data Visualization

The AI suggested that plots should contain labeled axes and units. I knew that I wanted plots, but explicitly requiring labels and units makes the requirement more useful and testable. I included this idea in my final requirements.

## 2. Standard Deviation

The AI suggested calculating standard deviation as part of the summary statistics. This is particularly useful for this application because standard deviation is also needed when calculating turbulence intensity.

## 3. Exporting Processed Results

The AI suggested exporting calculated statistics. I originally focused mainly on displaying results, but saving the processed information would be useful for reports and later analysis. I therefore added an export user story to the final requirements.

## 4. File Error Handling

The AI included an acceptance criterion requiring an error to be reported when a CSV file cannot be opened. This is a reasonable requirement that I retained and expanded to include malformed CSV data.

---

# Audit of the AI Non-Functional Requirements

The AI's non-functional requirements were the weakest portion of its response because most of them could not be falsified as written.

For example, the AI stated:

> "The application should process sensor data quickly."

There is no definition of "quickly," so there is no objective test that could determine whether the requirement has been satisfied. I replaced this with a measurable requirement stating that a dataset containing up to 100,000 rows and 16 sensor channels must be processed within 10 seconds on the development computer.

The AI also stated:

> "The user interface should be intuitive and easy to use."

Terms such as "intuitive" and "easy" are subjective without a defined usability test. I did not include this requirement in the current requirements document.

The AI stated:

> "Calculations should be accurate."

Again, "accurate" does not define an acceptable error. I replaced this with a requirement specifying that calculated values must be within 0.1% of independently calculated reference values.

Finally, the AI suggested supporting large CSV files without defining what qualifies as "large." I replaced this vague statement by defining a specific dataset size in the performance requirement.

---

# Conclusion

The AI produced a useful starting point, especially for identifying basic functionality such as CSV importing, plotting, statistics, and result exporting. However, it did not ask enough questions about the structure and limitations of the actual sensor data. It also introduced several features that were outside the intended scope of the project.

The biggest issue was that its non-functional requirements sounded reasonable but were not measurable. Auditing the generated requirements resulted in more specific requirements concerning input validation, multiple sensor channels, calculation accuracy, performance, and error handling. This demonstrated why AI-generated requirements still require engineering review rather than being accepted directly.
