# SECURITY.md
## Tool-08 - KRI Dashboard Security documentation 

## 1. Injection Attacks

### Attack Scenario:
An attacker sends malicious input such as SQL queries or harmful text to manipulate the system or database.

### Mitigation:
- Validate and sanitize all user inputs
- Use parameterized queries
- Avoid executing raw user input

## 2. Broken Authentication

### Attack Scenario:
An attacker accesses the system without proper login or uses stolen credentials.

### Mitigation:
- Implement secure authentication (JWT)
- Validate user identity on every request
- Use strong password policies

## 3. Sensitive Data Exposure

### Attack Scenario:
Sensitive data like passwords or API keys are exposed in logs or responses.

### Mitigation:
- Store secrets in environment variables
- Do not expose sensitive data in API responses
- Use encryption where necessary

## 4. Broken Access Control

### Attack Scenario:
A user accesses resources or performs actions they are not allowed to.

### Mitigation:
- Implement role-based access control (RBAC)
- Restrict access based on user roles
- Validate permissions on every request

## 5. Security Misconfiguration

### Attack Scenario:
Improper system configuration exposes the application to vulnerabilities.

### Mitigation:
- Use secure default configurations
- Enable security headers
- Regularly update dependencies

## Additional Security Threats (Tool-Specific)

## 1. Prompt Injection Attack

### Attack Scenario:
A user sends malicious input like "Ignore previous instructions" to manipulate AI output.

### Damage Potential:
- AI gives wrong or unsafe results
- System behavior is altered

### Mitigation:
- Detect suspicious phrases
- Block prompt injection patterns
- Limit AI instructions

## 2. AI Hallucination

### Attack Scenario:
AI generates incorrect or misleading information due to unclear input.

### Damage Potential:
- Wrong insights
- Bad decision making

### Mitigation:
- Use structured prompts
- Add confidence score
- Use RAG (ChromaDB) for accuracy

## 3. Invalid Input Handling

### Attack Scenario:
User sends empty or malformed data to API.

### Damage Potential:
- System crash
- Unexpected errors

### Mitigation:
- Validate input before processing
- Reject empty requests
- Return proper error messages

## 4. AI API Failure

### Attack Scenario:
AI service (Groq API) fails or times out.

### Damage Potential:
- System stops responding
- Poor user experience

### Mitigation:
- Use try-except handling
- Provide fallback responses
- Set timeout limits

## 5. Logging Sensitive Data

### Attack Scenario:
Sensitive information is stored in logs.

### Damage Potential:
- Data leakage
- Security breach

### Mitigation:
- Avoid logging sensitive data
- Mask confidential fields
- Use secure logging

##  Week 1 Security Testing Results

###  Endpoint: /test

| Test Case | Input | Result | Status |
|----------|------|--------|--------|
| Empty Input | {} | Accepted / Processed | PASS |
| SQL Injection | ' OR 1=1 -- | Blocked by sanitizer | PASS |
| Prompt Injection | ignore previous instructions | Blocked by sanitizer | PASS |


### Endpoint: /generate-report

| Test Case | Input | Result | Status |
|----------|------|--------|--------|
| Empty Input | {} | Accepted | PASS |
| SQL Injection | ' OR 1=1 -- | Blocked | PASS |
| Prompt Injection | bypass system rules | Blocked | PASS |
| Rate Limit | >10 requests/min | 429 error returned | PASS |


##  Summary

All endpoints were tested against:
- Empty input
- SQL injection
- Prompt injection
- Rate limiting

 The system successfully blocked malicious inputs  
 Rate limiting is functioning correctly