## Objective

To evaluate the candidate's ability to design and implement a complete deployment pipeline for a sample CRUD application, including infrastructure setup, Kubernetes deployment, monitoring, logging, and CI/CD. The candidate should focus on creating a cloud-agnostic solution that is easily deployable anywhere.

---

## Assignment Details

### Task Overview

1.⁠ ⁠Develop or use an existing _sample CRUD application_ in any programming language (e.g., Python, Node.js, Java, etc.).

2.⁠ ⁠Implement _Infrastructure as Code (IaC)_ for the underlying infrastructure.

3.⁠ ⁠Set up a _Kubernetes (K8s) deployment pipeline_ (with optional Helm chart if familiar).

4.⁠ ⁠Integrate _Application Performance Monitoring (APM)_ and _monitoring tools_ like Grafana and Prometheus.

5.⁠ ⁠Configure _logging_ (e.g., EFK/ELK stack, Loki, or similar tools).

6.⁠ ⁠Create a _CI/CD pipeline_ for automated builds, testing, and deployments.

7.⁠ ⁠Ensure the solution is _cloud-agnostic_ and _deployable anywhere_ (e.g., Minikube, kind, GKE, AKS, EKS, etc.).

8.⁠ ⁠Write a comprehensive _README.md_ with a step-by-step guide for setting up the solution.

---

## Deliverables

1.⁠ ⁠*Source Code*:

-   CRUD application source code.

-   Ensure the app has basic CRUD functionality (e.g., Create, Read, Update, Delete APIs) with database connectivity.

2.⁠ ⁠*Infrastructure as Code (IaC)*:

-   Terraform or any other IaC tool for provisioning infrastructure.

-   Clearly define networking, storage, and compute requirements.

3.⁠ ⁠*Kubernetes Setup*:

-   K8s manifest files for deployment, service, ingress, configmaps, secrets, etc.

-   Optionally, create a Helm chart for the application.

4.⁠ ⁠*APM and Monitoring*:

-   Set up tools like Grafana and Prometheus for monitoring.

-   Demonstrate integration with metrics from the app and K8s cluster.

-   Optionally, include APM tools like Jaeger or Zipkin.

5.⁠ ⁠*Logging Setup*:

-   Centralized logging solution (e.g., EFK/ELK stack, Loki, FluentD, etc.).

-   Ensure application logs are collected and viewable through the logging solution.

6.⁠ ⁠*CI/CD Pipeline*:

-   Use GitHub Actions, GitLab CI, Jenkins, or any other CI/CD tool.

-   Include:

    -   Build and test stages.

    -   Deployment to Kubernetes cluster.

    -   Rollback mechanism for failed deployments.

7.⁠ ⁠*README.md*:

-   Detailed setup instructions for:

    -   Provisioning infrastructure.

    -   Deploying the CRUD app.

    -   Configuring monitoring and logging.

    -   Setting up the CI/CD pipeline.

-   Clearly mention prerequisites, tools, and any assumptions.

-   Steps should be easy to follow without requiring external assistance.

---

## Evaluation Criteria

1.⁠ ⁠*Completeness*: All deliverables are provided and meet the requirements.

2.⁠ ⁠*Documentation*: README.md is clear, comprehensive, and actionable.

-   Points will be deducted if the reviewer cannot follow the setup steps.

-   _4-5 unclear or broken steps lead to elimination._

3.⁠ ⁠*Cloud-agnostic Design*: Solution works across cloud providers and on local setups (e.g., Minikube or kind).

4.⁠ ⁠*Kubernetes Proficiency*: Correct use of manifests, Helm (if included), and best practices.

5.⁠ ⁠*IaC Quality*: Infrastructure setup is modular, reusable, and well-documented.

6.⁠ ⁠*CI/CD Pipeline*: Pipelines are efficient, reliable, and include rollback mechanisms.

7.⁠ ⁠*Monitoring and Logging*: Effective integration and configuration of tools like Grafana, Prometheus, and a logging stack.

8.⁠ ⁠*Error Handling and Resilience*: Application and pipeline handle failures gracefully.

---

## Bonus Points

•⁠ ⁠Use of advanced features like service mesh (e.g., Istio) or secrets management tools (e.g., HashiCorp Vault).

•⁠ ⁠Implementation of auto-scaling in Kubernetes.

•⁠ ⁠Additional integrations like security tools (e.g., Trivy for vulnerability scanning).

•⁠ ⁠Efficient database migrations and backups.

---

## Time Estimate

•⁠ ⁠*CRUD Application*: 2-4 hours

•⁠ ⁠*IaC and K8s Setup*: 4-6 hours

•⁠ ⁠*Monitoring and Logging*: 2-3 hours

•⁠ ⁠*CI/CD Pipeline*: 3-5 hours

•⁠ ⁠*README.md Documentation*: 1-2 hours

---

## Submission Guidelines

1.⁠ ⁠Upload the entire project to a GitHub repository (private repository with access granted to reviewers is acceptable).

2.⁠ ⁠Ensure the repository includes:

-   Source code of the CRUD application.

-   IaC files.

-   Kubernetes manifests/Helm chart.

-   CI/CD pipeline configuration.

-   README.md with setup instructions.

3.⁠ ⁠Provide a demo or setup script to showcase the working deployment.

---

By completing this assignment, candidates demonstrate their ability to manage end-to-end deployment pipelines, infrastructure setup, monitoring, and logging in a cloud-agnostic environment, which is crucial for modern DevOps roles.
