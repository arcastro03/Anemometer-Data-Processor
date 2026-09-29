# Prompt-and-Diff Log

## Entry 1 – Requirements Elicitation

### Prompt

I am developing an application that processes CSV files containing data from pressure transducer sensors used to measure wind. The pressure measurements can be converted into wind velocity. I want the program to process experimental data and provide useful information such as average wind speed, turbulence intensity, and plots.

Elicit software requirements for this application. Provide user stories with acceptance criteria and suggest non-functional requirements.

### AI Contribution

The AI generated an initial set of functional requirements, user stories, acceptance criteria, and non-functional requirements. It suggested functionality including CSV importing, pressure-to-velocity conversion, statistical analysis, turbulence intensity calculations, plotting, exporting results, and saving experiments.

### Changes Made After Review

I reviewed the generated requirements rather than accepting them directly.

I added:
- Explicit validation of missing and invalid sensor data.
- Support for multiple sensor channels.
- Required-column validation.
- Handling of zero mean velocity during turbulence intensity calculations.
- Protection of the original experimental CSV file.
- Measurable performance and calculation-accuracy requirements.

I removed or rejected:
- A built-in experiment management system.
- Required zooming and panning of plots.
- Required PNG graph export.
- Required Windows, macOS, and Linux compatibility.

I also replaced vague AI-generated non-functional requirements such as "the application should be fast" and "calculations should be accurate" with measurable requirements containing specific thresholds.

### Result

The final requirements are narrower than the AI-generated requirements but are more closely aligned with the actual sensor-data-processing application and are more testable.
