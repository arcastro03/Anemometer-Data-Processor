PROMPT AND DIFF LOG
===================

Prompt:
Create a domain model for a Python application that imports CSV
files containing pressure-transducer wind sensor data. The
application validates the CSV, converts pressure in inches of
water to wind velocity, calculates statistics including average
wind speed and turbulence intensity, supports multiple sensor
channels, generates plots, and exports processed results.
Produce the model as a Mermaid class diagram.

AI Draft:
The generated model contained the following classes:

- User
- Role
- Permission
- Project
- Dataset
- Sensor
- Measurement
- Analysis
- Plot
- Export
- Settings
- AuditLog

Changes Made:
- Removed User
- Removed Role
- Removed Permission
- Removed Project
- Removed Settings
- Removed AuditLog
- Removed Plot as a domain entity
- Removed Export as a domain entity
- Renamed Sensor to SensorChannel
- Renamed Measurement to Sample
- Renamed Analysis to AnalysisResult
- Added Dataset validation status and validation errors
- Added pressure-to-velocity behavior to SensorChannel
- Added explicit Dataset -> SensorChannel -> Sample relationships
- Added SensorChannel -> AnalysisResult relationship

Reason:
The removed classes were not supported by any M2 requirement.
The final model focuses only on objects necessary to import,
validate, process, analyze, plot, and export wind sensor data.
