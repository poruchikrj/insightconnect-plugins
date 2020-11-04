
## Assessment
### Run

<details>

```
{
  "body": {
    "log": "Connect: Connecting...\nrapid7/DNS:2.0.0. Step name: forward\nExecuting command /usr/bin/dig @8.8.8.8 rapid7.com MX\n",
    "meta": {},
    "output": {
      "all_answers": [
        "aspmx.l.google.com",
        "alt3.aspmx.l.google.com",
        "alt4.aspmx.l.google.com",
        "alt1.aspmx.l.google.com",
        "alt2.aspmx.l.google.com"
      ],
      "answer": "aspmx.l.google.com",
      "fulloutput": "\n; \u003c\u003c\u003e\u003e DiG 9.14.12 \u003c\u003c\u003e\u003e @8.8.8.8 rapid7.com MX\n; (1 server found)\n;; global options: +cmd\n;; Got answer:\n;; -\u003e\u003eHEADER\u003c\u003c- opcode: QUERY, status: NOERROR, id: 30462\n;; flags: qr rd ra; QUERY: 1, ANSWER: 5, AUTHORITY: 0, ADDITIONAL: 1\n\n;; OPT PSEUDOSECTION:\n; EDNS: version: 0, flags:; udp: 512\n;; QUESTION SECTION:\n;rapid7.com.\t\t\tIN\tMX\n\n;; ANSWER SECTION:\nrapid7.com.\t\t215\tIN\tMX\t1 aspmx.l.google.com.\nrapid7.com.\t\t215\tIN\tMX\t10 alt3.aspmx.l.google.com.\nrapid7.com.\t\t215\tIN\tMX\t10 alt4.aspmx.l.google.com.\nrapid7.com.\t\t215\tIN\tMX\t5 alt1.aspmx.l.google.com.\nrapid7.com.\t\t215\tIN\tMX\t5 alt2.aspmx.l.google.com.\n\n;; Query time: 52 msec\n;; SERVER: 8.8.8.8#53(8.8.8.8)\n;; WHEN: Wed Nov 04 07:39:11 UTC 2020\n;; MSG SIZE  rcvd: 154\n\n",
      "last_answer": "alt2.aspmx.l.google.com",
      "nameserver": "8.8.8.8",
      "question": "rapid7.com",
      "status": "NOERROR"
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/dns:2.0.0 --debug run < tests/forward.json
</summary>
</details>

<details>

```
{
  "body": {
    "log": "Connect: Connecting...\nrapid7/DNS:2.0.0. Step name: reverse\nExecuting command /usr/bin/dig @8.8.8.8 -x 1.2.3.4\n",
    "meta": {},
    "output": {
      "answer": "Not found",
      "fulloutput": "Resolution failed, nameserver 8.8.8.8 returned NXDOMAIN status",
      "nameserver": "8.8.8.8",
      "question": "1.2.3.4",
      "status": "NXDOMAIN"
    },
    "status": "ok"
  },
  "type": "action_event",
  "version": "v1"
}

```

<summary>
docker run --rm -i rapid7/dns:2.0.0 --debug run < tests/reverse.json
</summary>
</details>

<details>

```
[*] Validating plugin with all validators at .

[*] Running Integration Validators...
[*] Executing validator HelpValidator
[*] Executing validator ChangelogValidator
[*] Executing validator RequiredKeysValidator
[*] Executing validator UseCaseValidator
[*] Executing validator SpecPropertiesValidator
[*] Executing validator SpecVersionValidator
[*] Executing validator FilesValidator
[*] Executing validator TagValidator
[*] Executing validator DescriptionValidator
[*] Executing validator TitleValidator
[*] Executing validator VendorValidator
[*] Executing validator DefaultValueValidator
[*] Executing validator IconValidator
[*] Executing validator RequiredValidator
[*] Executing validator VersionValidator
[*] Executing validator DockerfileParentValidator
[*] Executing validator LoggingValidator
[*] Executing validator ProfanityValidator
[*] Executing validator AcronymValidator
[*] Executing validator JSONValidator
[*] Executing validator OutputValidator
[*] Executing validator RegenerationValidator
[*] Executing validator HelpInputOutputValidator
[*] Executing validator SupportValidator
[*] Executing validator RuntimeValidator
[*] Executing validator ExceptionValidator
[*] Executing validator CredentialsValidator
[*] Executing validator PasswordValidator
[*] Executing validator PrintValidator
[*] Executing validator ConfidentialValidator
[*] Executing validator DockerValidator
[*] Executing validator URLValidator
WARNING: URLs found that return a 4xx code. Verify they are publicly accessible and if not, update with a working URL.
violation: help.md[165]: https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml
violation: help.md[216]: https://www.iana.org/assignments/dns-parameters/dns-parameters.xhtml
[*] Plugin successfully validated!

----
[*] Total time elapsed: 42764.65ms
```

<summary>
icon-validate --all .
</summary>
</details>

<details>

```
[*] Use ``make menu`` for available targets
[*] Including available Makefiles: ../tools/Makefiles/Helpers.mk ../tools/Makefiles/Colors.mk
--
[*] Running validators
[*] Validating plugin at .

[*] Running Integration Validators...
[*] Executing validator HelpValidator
[*] Executing validator ChangelogValidator
[*] Executing validator RequiredKeysValidator
[*] Executing validator UseCaseValidator
[*] Executing validator SpecPropertiesValidator
[*] Executing validator SpecVersionValidator
[*] Executing validator FilesValidator
[*] Executing validator TagValidator
[*] Executing validator DescriptionValidator
[*] Executing validator TitleValidator
[*] Executing validator VendorValidator
[*] Executing validator DefaultValueValidator
[*] Executing validator IconValidator
[*] Executing validator RequiredValidator
[*] Executing validator VersionValidator
[*] Executing validator DockerfileParentValidator
[*] Executing validator LoggingValidator
[*] Executing validator ProfanityValidator
[*] Executing validator AcronymValidator
[*] Executing validator JSONValidator
[*] Executing validator OutputValidator
[*] Executing validator RegenerationValidator
[*] Executing validator HelpInputOutputValidator
[*] Executing validator SupportValidator
[*] Executing validator RuntimeValidator
[*] Plugin successfully validated!

----
[*] Total time elapsed: 954.704ms

[*] Validating spec with js-yaml
[SUCCESS] Passes js-yaml spec check


[*] Validating markdown...
[SUCCESS] Passes markdown linting

[*] Validating python files for style...
[SUCCESS] Passes flake8 linting

[*] Validating python files for security vulnerabilities...
[main]	INFO	profile include tests: None
[main]	INFO	profile exclude tests: None
[main]	INFO	cli include tests: None
[main]	INFO	cli exclude tests: None
[main]	INFO	running on Python 3.7.3
Run started:2020-11-04 12:43:42.550147

Test results:
	No issues identified.

Code scanned:
	Total lines of code: 338
	Total lines skipped (#nosec): 0

Run metrics:
	Total issues (by severity):
		Undefined: 0.0
		Low: 0.0
		Medium: 0.0
		High: 0.0
	Total issues (by confidence):
		Undefined: 0.0
		Low: 0.0
		Medium: 0.0
		High: 0.0
Files skipped (0):
[SUCCESS] Passes bandit security checks

[*] For spell checking, install misspell: go get -u github.com/client9/misspell/cmd/misspell
```

<summary>
make validate
</summary>
</details>
