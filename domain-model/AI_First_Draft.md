classDiagram

class User {
    +userId: int
    +name: string
    +email: string
}

class Role {
    +roleId: int
    +name: string
}

class Permission {
    +permissionId: int
    +name: string
}

class Project {
    +projectId: int
    +name: string
    +createdAt: datetime
}

class Dataset {
    +datasetId: int
    +fileName: string
    +importDate: datetime
    +rowCount: int
}

class Sensor {
    +sensorId: int
    +name: string
    +type: string
    +calibrationFactor: float
}

class Measurement {
    +measurementId: int
    +timestamp: float
    +pressure: float
    +velocity: float
}

class Analysis {
    +analysisId: int
    +averageVelocity: float
    +turbulenceIntensity: float
    +minimumVelocity: float
    +maximumVelocity: float
    +standardDeviation: float
}

class Plot {
    +plotId: int
    +plotType: string
    +filePath: string
}

class Export {
    +exportId: int
    +format: string
    +filePath: string
}

class Settings {
    +settingsId: int
    +airDensity: float
    +units: string
}

class AuditLog {
    +logId: int
    +action: string
    +timestamp: datetime
}

User "1" --> "1" Role
Role "*" --> "*" Permission
User "1" --> "*" Project
Project "1" --> "*" Dataset
Dataset "1" --> "*" Sensor
Sensor "1" --> "*" Measurement
Dataset "1" --> "*" Analysis
Analysis "1" --> "*" Plot
Analysis "1" --> "*" Export
User "1" --> "1" Settings
User "1" --> "*" AuditLog
