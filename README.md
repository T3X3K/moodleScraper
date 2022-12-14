# Moodle Scraper
If you're using the Moodle.org platform for your Uni courses, this utility will allow you to download 
all files from your courses. So far, this software is built to work on University of Padoa's moodle page,
more precisely the stem.elearning page.

## Usage
From the command line use the command (after having downloaded the [required stuff](#required-stuff))
```bash
python3 moodleScraper.py <username> <password> <course_link> <path>
```
where: 
\<username\> is your username \
\<password\> is your password \
\<course_link\> is the link of the moodle page of the course \
\<path\> is the path where you want to download the files. For instance, for wsl users,
to download them in my desktop I use /mnt/c/Users/S3XYT3X3K/Desktop/ (not true, but you get the point). \
Actually, what I do is run the command
```bash
while true; do python3 moodleScraper.py <username> <password> <course_link> <path> && break; done
```
as I've explained [later](#crashes)

### Required Stuff
You'll need to install the selenium, beautifulsoup and requests libraries if you don't already have them,
using the pip or pip3 command, like:
```bash
pip install selenium requests beautifulsoup4
```

Also, you'll need to install what is called a chrome driver which will allow python to use google. 
This [youtube video](https://www.youtube.com/watch?v=2WVxzRD6Ds4) should help you. Update the path of
where you've installed in the webdriver_service, around line 20.

## Crashes 
So far, it crashes for two reasons
1. fails to login because sometimes it's naughty
2. has to open files with weird names

The simple solution for problem n. 1 is to execute multiple times the program until it works.
It can be annoying, so what I do is I use a while loop to tell the bash terminal to rerun the program 
until it works. This can be done this way:
```bash
while true; do ./out && break; done
```
where out is a bash file where I've written the command
```bash
python3 moodleScraper.py <username> <password> <course_link> <path>
```

### fails to login
The problem is with selenium. It doesn't send correctly the username or the password, or it doesn't click 
what is supposed to click. As it's random when it will work or not, you can just rerun the program a 
couple of times and it will work.

### has to open files with weird names
Originally, if the file had '(', ')' or '/' in its name, the program would crash. Now it will substitute this 
characters with others because of the 
`linkers.append([a['href'],a.get_text().replace('(','').replace(')','').replace(' ','_').replace('/','.')])'.
If you have any ideas on why this happens and you have a more general solution for this problem, 
feel free to help. 

## Future Plans
### Files extensions
When on the main course page, the program will download everythiing as pdf. Of course, in the future 
the program needs to assign the right extension to each file.

### Log
If you use some software to scribble on the pdfs, you will likely loose all your notes because this 
program will overwrite everything everytime it's used. On the other hand, some of your professors 
may continuosly upload the same files after making corrections, so you do want in some cases the program to 
re-download somethings. To solve this conundrum, I was thinking to add a log from where this program will know 
wether or not a file has already been downloaded and it doesn't need to do it again. Downloaded. 

### Subfolders
Maybe it would be nice if the scraper didn't just download all the files together. Rather, it may be cool
if it created subfolders. Have to think about it. 

### Password Problems
After a while, your password may expire. This program does not yet know when this happens. It would be 
important in future updates to understand when this occurs, and possibily to allow you to update it from 
command line prompt.

### safari and mozzila-driver
I guess not everybody uses chrome, and thus some people would prefer if there was the option to 
have another driver instead of the chromedriver

## Issues
### Type of files
So far, it assumes all files are pdfs. It's easy to improve it, but it will take some time. 

### Failed Login
You won't know when the login is successful. Sometimes, it will give the following error:
```bash
Traceback (most recent call last):
  File "moodleScraper.py", line 41, in <module>
    username = WebDriverWait(driver, t).until(EC.element_to_be_clickable(
  File "/home/behappy/.local/lib/python3.8/site-packages/selenium/webdriver/support/wait.py", line 78, in until
    value = method(self._driver)
  File "/home/behappy/.local/lib/python3.8/site-packages/selenium/webdriver/support/expected_conditions.py", line 326, in _predicate
    target = driver.find_element(*target)  # grab element at locator
  File "/home/behappy/.local/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 1248, in find_element
    return self.execute(Command.FIND_ELEMENT, {
  File "/home/behappy/.local/lib/python3.8/site-packages/selenium/webdriver/remote/webdriver.py", line 425, in execute
    self.error_handler.check_response(response)
  File "/home/behappy/.local/lib/python3.8/site-packages/selenium/webdriver/remote/errorhandler.py", line 247, in check_response
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
Originally, I saw this problem happens when the file [has to open files with weird names](#has-to-open-files-with-weird-names). 
Look into that part of the document.
