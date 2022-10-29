# moodleScraper
If you're using the Moodle.org platform for your Uni courses, this utility will allow you to download 
all files from your courses. So far, this software is built to work on University of Padoa's moodle page,
more precisely thei stem.elearning page.

## Comand
From the coman line use the command
```bash
python3 moodleScraper.py <username> <password>
```
where \<username\> is your username, while \<password\> is your password.

## Issues
### Password Problems
After a while, your password may expire. This program does not yet know when this happens. It would be 
important in future updates to understand when this occurs, and possibily to allow you to update it from 
command line prompt.
