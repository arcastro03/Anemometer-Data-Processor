classDiagram

class Dataset {
    +filePath: string
    +rowCount: int
    +validationStatus: string
    +validationErrors: string[]
    +validate()
    +process()
}

class SensorChannel {
    +name: string
    +pressureUnit: string
    +convertPressureToVelocity()
    +calculateStatistics()
}

class Sample {
    +timestamp: float
    +pressureInH2O: float
    +velocity: float
}

class AnalysisResult {
    +averageVelocity: float
    +turbulenceIntensity: float
    +minimumVelocity: float
    +maximumVelocity: float
    +standardDeviation: float
}

Dataset "1" *-- "1..*" SensorChannel : contains
SensorChannel "1" *-- "0..*" Sample : contains
SensorChannel "1" --> "0..1" AnalysisResult : produces
