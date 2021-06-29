# Python-behave

# Useful comments:
```
1. behave - to run all the testacses
2. behave ./features/<name>.feature - to run the particular feature
3. behave --tags=<tagname> - to run the specific scenarios
4. behave -D browser=<browser> - to pass user defines argument (stored in context.config.userdata)
5. behave -D [browser=chrome,env=stage] - to pass multiple arguments 
6. behave --no-capture --no-color - to see the print in terminal
7. behave -f allure_behave.formatter:AllureFormatter -o reports_folder /featurename.feature
8. allure generate json_folder -o convert_to_html_folder - to generate html report from json
```

# To install allure in linux
```gherkin
1. sudo apt-get install -y allure
2. allure --version - to check version
3. If you see "bash allure Not Found" run below command,
    a. export PATH=$PATH:/opt/allure-2.13.8/bin/

```
