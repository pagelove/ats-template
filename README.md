# Pagelove ATS template

Public source: [pagelove/ats-template](https://github.com/pagelove/ats-template). This repository carries the prepared ATS implementation and its source history. The original pagelove/pagelove-ats repository is preserved. Publishing this code does not establish native hosted application permissions or intake acceptance.

This native HTML template keeps roles, candidates and activity records in its source documents. Read [the document-first project record](DOCUMENT-FIRST-REVIEW.md), site/README.html and site/admin/auth.html before installation. Preserve the parameterized site/roles/:role_name/index.html route; Windows requires a checkout mechanism that can preserve or extract this Git path, such as a Linux environment. Do not rename the native route to make a Windows checkout pass.

Run python scripts/check-document-first.py for source identity and inline-script syntax checks. Actual composed routes, application intake, permissions, concurrency and delivery require verification on the target Pagelove host. Use fictional records until those gates pass.
