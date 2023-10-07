# Moodle Scraper
If you're using the Moodle.org platform for your Uni courses, this utility will allow you to download 
all files from your courses. So far, this program is built to work on University of Padoa's moodle page,
more precisely the stem.elearning page.

## Usage
From the command line use the command (after having downloaded the [required stuff](#required-stuff))
```bash
python3 moodleScraper.py <username> <password> <course_link_1> <path_1> <course_link_2> <path_2> ...
```
where: 
\<username\> is your username \
\<password\> is your password \
\<course_link_1\> is the link of the moodle page of the first course \
\<path_1\> is the path where you want to download the first course's files. For instance, for wsl users,
to download them in my desktop I use /mnt/c/Users/T3X3K/Desktop/
You can actually download more than one course at a time, as you see in the example.

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
3. bonus: expired password

Luckily, 99% it crashes because of problem n. 1. The simple solutio is to execute multiple times
the program until it works.
It can be annoying, so what I do is I use a while loop to tell the bash terminal to rerun the program 
until it works. This can be done this way:
```bash
while true; do ./out && break; done
```
where out is a bash file where I've written the command
```bash
python3 moodleScraper.py <username> <password> <course_link> <path>
```

### Fails to login
The problem is with selenium. It doesn't send correctly the username or the password, or it doesn't click 
what is supposed to click. As errors occur randomly, you can just rerun the program a 
couple of times and it will work.

### Has to open files with weird names
Originally, if the file had '(', ')' or '/' in its name, the program would crash. Now it will substitute this 
characters with others because of the 
`linkers.append([a['href'],a.get_text().replace('(','').replace(')','').replace(' ','_').replace('/','.')])'.
If you have any ideas on why this happens and you have a more general solution for this problem, 
feel free to help. It hasn't happened in a while, and I've started to think it was just a coincidence and
something else might have been the problem. Dunno, should check someday.

### Expired password

Only now that I'm updating the code this problem might have come up. Because so much other stuff
was going on, I'm not entirely sure this was the problem, but it could be. The program doesn't
know how to understand if the password has expired, so it won't tell you anything about it,
but realistically you'll find out you need to change your password without the need of
the scraper (personally speaking at least). Hence, I'm not doing anything about it, but I'm
happy if you want to contribute.

## Future Plans
### Files extensions
When on the main course page, the program will download everything as pdf. Of course, in the future 
the program needs to assign the right extension to each file.

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

## FAQ

If I modify a file, will the scrape overwrite the edits while redownloading it?
The program now checks whether or not the file has been uploaded to the moodle after the last time you've
scraped it. If it hasn't, it doesn't download it. If the file on moodle has been modified, the scraper
will download it without overwriting the previus file.

Does it download videos?
It actually doesn't do so, but adding this feature shouldn't be a problem. It's just that we never needed it.

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

# Google.py

Little utility, found it on Tiff in Tech's youtube video (also present in some other tutorial).
It will quickly print on the command line around ten results (title, url, description) of a google search of your choice.
Actually, ten in italian and ten in english.

For instance, if you want to know who Gregg Popovich is you can run the following command

```bash
python google.py gregg popovich
```

the first results you'll get shoul look like

```bash
GREGG POPOVICH  https://it.wikipedia.org/wiki/Gregg_Popovich
Gregg Charles Popovich (East Chicago, 28 gennaio 1949) è un allenatore di pallacanestro e dirigente sportivo statunitense di origine serba e croata, ...
GREGG POPOVICH  https://en.wikipedia.org/wiki/Gregg_Popovich
Gregg Charles Popovich (born January 28, 1949) is an American professional basketball coach and executive who is the president and head coach 
```

Actually, thanks to the termcolor package, the text you see should be coloured, to improve readibilty.

## Required Packages

You'll need the googlesearch package for sure; on top of that, you might need the termcolor one

```bash
pip install googlesearch-python termcolor
```
