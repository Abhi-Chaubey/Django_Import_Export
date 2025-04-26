A Report Generator microservice given by NATWEST GROUP:

Functional Requirements:
1.	Implement using a framework of your choice: FastAPI/Flask/Django
2.	Provide REST endpoints to: done
3.	Upload input.csv and reference.csv: done
4.	Trigger report generation on-demand: done
5.	Download generated reports: done
6.	End points to configure  transformation rules: done
7.	Ability to define schedules using cron expressions or configuration: notdone
8.	Read transformation rules from a JSON or YAML config file: notdone
9.	Easily extend to support new formats like Excel (.xlsx) and JSON: done

Non Functional Requirements
1.	Authentication, Authorization: done
2.	Monitoring and observability: notdone
3.	Structured logging: notdone
4.	Unit tests and Test coverage: done
5.	Leverage docker for deployment and dependent services(database): notdone
6.	Must be able to generate a report from a 1 GB file in under 30 seconds: trying
7.	Handle up to 250 fields in input/output files: trying
