# Wind Sensor Data Processor

## Concept Brief

The Wind Sensor Data Processor is an application designed to process experimental data collected from pressure transducer sensors used for wind measurements. The sensors measure differential pressure in inches of water (`inH2O`), which can be converted into wind velocity using the appropriate pressure-to-velocity relationship. The application will import recorded sensor data from CSV files and process it into useful aerodynamic and statistical information. Planned features include calculating average wind speed, turbulence intensity, pressure and velocity statistics, and generating plots that help visualize wind behavior over the duration of an experiment. The goal is to create a repeatable analysis workflow that reduces the amount of manual processing required after collecting wind-sensor data.

## Declared Stack

* **Language:** Python 3
* **Package Manager:** pip
* **Data Processing:** pandas and NumPy
* **Plotting:** Matplotlib
* **Test Runner:** pytest
* **Version Control:** Git and GitHub
* **AI Coding Tool:** ChatGPT

## Planned Features

* Import sensor data from CSV files
* Parse pressure-transducer measurements
* Convert pressure measurements to wind velocity
* Calculate average wind velocity
* Calculate turbulence intensity
* Calculate basic statistics such as minimum, maximum, mean, and standard deviation
* Generate wind-speed versus time plots
* Generate pressure versus time plots
* Export processed results

## Current Status

This repository currently contains the initial project structure and toolchain verification for the application. Analysis features will be implemented in later development milestones.
