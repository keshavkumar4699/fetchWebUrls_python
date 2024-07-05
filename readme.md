# This projects fetches the list of downloadable items from website

### Objectives of this Project
1. Search for all torrents in table if they are freeleech or not if yes then download them
2. Search for 150 VIP torrents less than 1MB and download them
3. Search for 100 freeleech torrents less than 1MB and download them

### STEPS followed
#### Objective 1: For fetching from snatch table
1. Go to torrents page 'https://www.myanonamouse.net/snatch_summary.php'
2. Expand the content of 'Satisfied Not seeding'
3. Get the list of torrents

#### Objective 2: For fetching list of VIP torrents
1. Go to torrents page 'https://www.myanonamouse.net/tor/browse.php'
2. Check in table for VIP torrent with size less than 2 MiB
3. Add them to array 

#### Objective 3: For fetching list of freeleech torrents
1. 

#### For downloading torrents
1. LogIN to site
2. Go to every torrent site
3. Check condition
4. Download them
5. Continue 2-4 until all filtered torrents downloaded
6. After each torrent is checked log out
7. Quit browser

##### Conditions
Objective 1: if freeleech or less than 1MB
Objective 2: if VIP and less than 1MB
Objective 3: if freeleech and less than 1MB

### Future Scope
1. Remove the need for snatch table and fetch directly from web and then download them
2. 