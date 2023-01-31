# Auth Microservice Design

### Summary

As a user, I would like third-party authorization of my Django session,
so that I can access elevated privileges appropriately.

### Constraints

1. Third party permissions should be provided as a function of username substring.
   1. This constraint is allowable because this is a toy application. Generally, this would not be a good commercial practice.
   2. This practice may be used in commercial staging environments for test usage.
   3. This approach simulates something like a real commercial LDAP or SSO.
2. This auth microservice should not use a DB. It should be stateless.

### Preferred Solution

This may include narrative, pseudocode methods, type definitions, and payload samples.

The preferred solution is to create a Flask endpoint that returns a rolename property with a value of "ADMIN" if the Django username includes the substring "admin". In all other cases, the third party authorization tool should return a value of "NONADMIN".

Guest access is controlled on the Django side. The third party tool doesn't know about guest usage, and shouldn't even be consulted about guest permissions.

### Alternatives Considered

We also thought about using FastAPI instead of Flask.

TODO: Why didn't we pick that?

### Risks

1. If this solution is deployed in a commercial production setting, it could allow users to obtain inappropriate authorization. Even in a toy environment, users may obtain unintended authorization simply because of the coupling of permission to username.
2. This solution requires a redeployment of code in order to change user permissions, unlike a solution that would use a DB.
