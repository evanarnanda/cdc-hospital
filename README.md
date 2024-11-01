# Change Data Capture Steaming

## Background

So this Hospital X have several Apps that are used to record patient data. For this mockup we will stored in a single Postgres database. For the starters we will use the following tables:

### Electric Health Records (EHR) System
- Patients
- Allergies
- Medications
- Doctor Notes
- Visits

### Hospital System
- Patients
- Doctors
- Doctor Notes
- Visits
- Pharmacy Orders
- Medications

## Project Mockup Flow

The EHR system will be the source of truth for the data. EHR is provided by goverment and is the source of truth for patient data. Hospital can use only the EHR database to read the data.

1. Data Generator will update the EHR database with the data.
2. Hospital will develop CDC pipeline to read the data from EHR database.
3. Hospital will update the Hospital database with the data from Pipeline.


## Project Tools

### Environment Tools
- [nixOs](https://nixos.org/) - We will use nix-shell to setup the environment.
- [docker-compose](https://docs.docker.com/compose/) - We will use docker-compose to run the several services.

### Data Tools
all of services will run on docker containers.
- [Postgres](https://www.postgresql.org/) - We will use Postgres to store the data.
- [Debezium](https://debezium.io/) - We will use Debezium to stream the data from Postgres to Kafka.
- [Kafka](https://kafka.apache.org/) - We will use Kafka to stream the data from Debezium to the Hospital.
- [Apache Spark](https://spark.apache.org/) - We will use Spark to process the data.

### Language
- [Python](https://www.python.org/) - We will use Python to generate the data.
- [UV](https://docs.astral.sh/uv/) - We will use UV for Python Package Manager.
- [Ruff](https://docs.astral.sh/ruff/) - We will use Ruff for Python Linter.

## How to run it
Assume you have installed NixOs and Docker.

Terminal 1:

```bash
nix-shell
```

Terminal 2:
```bash
docker-compose up -d
```

in NixOs terminal:

**uv sync** to sync project dependencies.
**uv run [script]** to run the project.

for more details, please refer to the [uv documentation](https://docs.astral.sh/uv/getting-started/features/).