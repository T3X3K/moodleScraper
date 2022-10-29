# moodleScraper
If you're using the Moodle.org platform for your Uni courses, this utility will allow you to download 
all files from your courses. So far, this software is built to work on University of Padoa's moodle page,
more precisely thei stem.elearning page.

## Comand
From the coman line use the command
```bash
python3 moodleScraper.py <username> <password> <course_link>
```
where: 
\<username\> is your username
\<password\> is your password
\<course_link\> is the link of the moodle page of the course. 

## Future Plans
### Password Problems
After a while, your password may expire. This program does not yet know when this happens. It would be 
important in future updates to understand when this occurs, and possibily to allow you to update it from 
command line prompt.

## Issues
### Failed Login
You won't know when the login is successful. Sometimes, it will give the following error:
```bash
Traceback (most recent call last):
  File "moodleScraper.py", line 41, in <module>
    username = WebDriverWait(driver, t).until(EC.element_to_be_clickable(
  File "/home/toxin21/.local/lib/python3.8/site-packages/selenium/webdriver/support/wait.py", line 78, in until
    value = method(self._driver)
  File "/home/toxin21/.local/lib/python3.8/site-packages/selenium/webdriver/support/expected_conditions.py", line 326, in _predicate
    target = driver.find_element(*target)  # grab element at locator
  File "/home/toxin21/.local/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 1248, in find_element
    return self.execute(Command.FIND_ELEMENT, {
  File "/home/toxin21/.local/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 425, in execute
    self.error_handler.check_response(response)
  File "/home/toxin21/.local/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py", line 247, in check_response
    raise exception_class(message, screen, stacktrace)
selenium.common.exceptions.InvalidArgumentException: Message: invalid argument: invalid locator
  (Session info: chrome=103.0.5060.114)
Stacktrace:
#0 0x5599b7031b13 <unknown>
#1 0x5599b6e38688 <unknown>
#2 0x5599b6e6f6d2 <unknown>
#3 0x5599b6e6fe91 <unknown>
#4 0x5599b6ea2e34 <unknown>
#5 0x5599b6e8d8dd <unknown>
#6 0x5599b6ea0b94 <unknown>
#7 0x5599b6e8d7a3 <unknown>
#8 0x5599b6e630ea <unknown>
#9 0x5599b6e64225 <unknown>
#10 0x5599b70792dd <unknown>
#11 0x5599b707d2c7 <unknown>
#12 0x5599b706322e <unknown>
#13 0x5599b707e0a8 <unknown>
#14 0x5599b7057bc0 <unknown>
#15 0x5599b709a6c8 <unknown>
#16 0x5599b709a848 <unknown>
#17 0x5599b70b4c0d <unknown>
#18 0x7fe73b275609 <unknown>
```

### FileNotFoundError
The program is supposed to find the files and their names, then open a new file with the same name in your computer. For some files though it gives the following error:
```bash
Traceback (most recent call last):
  File "moodleScraper.py", line 88, in <module>
    open(name[:size-5]+".pdf", 'wb').write(response.content)
FileNotFoundError: [Errno 2] No such file or directory: 'Calendario delle lezioni (modificato il 24/10/2022).pdf'
```
