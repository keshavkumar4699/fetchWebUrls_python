from bs4 import BeautifulSoup
import urllib.request

html_table = """
<table class="newTorTable" id="inactSat">
    <tbody>
        <tr>
            <td><a class="newCatLink" href="/tor/browse.php?tor[cat][]]=75">
                    <div class="cat75">&nbsp;</div>
                </a></td>
            <td></td>
            <td><a href="/t/1042472" class="torTitle">New Happy: Getting Happiness Right in a World That's Got It
                    Wrong</a> by <a class="author" href="/tor/browse.php?author=112468">Stephanie Harrison</a><br><span
                    class="torRowDesc">Self-Help &gt; Emotional Self-Help. Published May 14, 2024</span><br><span
                    class="torFileTypes"><a>epub</a></span> | 0 comments<br>
                <div class="browseInactSeed">Previously Seeding</div>
            </td>
            <td><a class="directDownload"
                    href="/tor/download.php/XBqK1a7BzRcka2iXNzMtRM2B0J+L2SIhFct4Q00OwH2ZqyShWGxWBSsRUgTINONgCNIT8QC3YE3fHpXSUiaMfQAjsC0MYFnUSTlR3w+a6CHVVtsCtInADIfrMArNOh4RNkCi5dtfPSPiR8ESkEp76X4T+zXy1TuN7yjzHQvS2h6xh6DZJLMDKMCa"
                    title="Direct Download" alt="Direct Download"> </a></td>
            <td>
                <p>0.0 KiB</p>
                <p>14.3 MiB</p>
                <p>0.000</p>
            </td>
            <td><span title="2024-06-22 17:36:11">2024-06-22</span><br>0:00<br><span
                    title="2024-06-22 17:36:19">2024-06-22</span><br><span class="row1-darkg">3d&nbsp;00:10:17</span>
            </td>
            <td>
                <p>126</p>
                <p>0</p>
                <p>173</p>
            </td>
        </tr>
        <tr>
            <td><a class="newCatLink" href="/tor/browse.php?tor[cat][]]=91">
                    <div class="cat91">&nbsp;</div>
                </a></td>
            <td><img alt="Contains Some Explicit Sex Scenes" title="Contains Some Explicit Sex Scenes"
                    src="https://cdn.myanonamouse.net/pic/lipssmall.png"></td>
            <td><a href="/t/1039506" class="torTitle">Guide To Getting It On: Unzipped - 9th Edition</a> by <a
                    class="author" href="/tor/browse.php?author=42157">Paul Joannides</a><br><span
                    class="torRowDesc">Sexuality; Publisher: Goofy Foot Press, 9th edition, 2018</span><br><span
                    class="torFileTypes"><a>pdf</a></span> | 0 comments<br>
                <div class="browseInactSeed">Previously Seeding</div>
            </td>
            <td><a class="directDownload"
                    href="/tor/download.php/jHAykqhMeZxj2gpMcwifl2MxU6+zp9EHbrZ9my+,,BxmR2Ga1hl1x0oDbv,p2E,Q,zngE67cQAMkZSNXwgLgFIh6z4Cpoojip7eDKkEsZNSA1Zx1l8JjY6jEGLkVL8CC+m1qmfdJvoirmgqXhZPN1FkJmD4XwjeiBV7eeOTRD4YLKyAkQNtIubpl"
                    title="Direct Download" alt="Direct Download"> </a></td>
            <td>
                <p>0.0 KiB</p>
                <p>28.4 MiB</p>
                <p>0.000</p>
            </td>
            <td><span title="2024-06-22 17:49:03">2024-06-22</span><br>0:00<br><span
                    title="2024-06-22 17:49:27">2024-06-22</span><br><span class="row1-darkg">3d&nbsp;00:06:36</span>
            </td>
            <td>
                <p>123</p>
                <p>0</p>
                <p>198</p>
            </td>
        </tr>
        <tr>
            <td><a class="newCatLink" href="/tor/browse.php?tor[cat][]]=75">
                    <div class="cat75">&nbsp;</div>
                </a></td>
            <td></td>
            <td><a href="/t/1022833" class="torTitle">Adult ADHD Tools (3 books in 1) Executive Functioning Workbook,
                    Mastering Concentration, Organization and Cleaning: Strengthen Focus, Memory, and Emotional ... and
                    Long Term</a> by <a class="author" href="/tor/browse.php?author=489087">Calvin Caufield</a><br><span
                    class="torRowDesc">Publication Date: September 19 2023, ADHD, Executive Functioning</span><br><span
                    class="torFileTypes"><a>epub</a></span> | 0 comments<br>
                <div class="browseInactSeed">Previously Seeding</div>
            </td>
            <td><a class="directDownload"
                    href="/tor/download.php/8g4l5jpgRpm9BbgSG2PUzjlerW3YOeXIR94gv,ntTlLHNfGdZiyRHjsQ8ciwc3X454h3VpxWBZPhyZJpvrya,X0cFF5rQjRvSgV31qw6jrNsDfNtEsB9usxJzBGbfRKm1kwgpkRDzMrRXeX8aPcqmrGahIHZ3V5ZdNoE8ykg5JcCjlAGs2ASVwoJ"
                    title="Direct Download" alt="Direct Download"> </a></td>
            <td>
                <p>0.0 KiB</p>
                <p>7.8 MiB</p>
                <p>0.000</p>
            </td>
            <td><span title="2024-06-22 17:35:01">2024-06-22</span><br>0:00<br><span
                    title="2024-06-22 17:35:10">2024-06-22</span><br><span class="row1-darkg">3d&nbsp;00:17:28</span>
            </td>
            <td>
                <p>150</p>
                <p>0</p>
                <p>257</p>
            </td>
        </tr>
        <tr>
            <td><a class="newCatLink" href="/tor/browse.php?tor[cat][]]=102">
                    <div class="cat102">&nbsp;</div>
                </a></td>
            <td></td>
            <td><a href="/t/1016407" class="torTitle">The Death Pit</a> by <a class="author"
                    href="/tor/browse.php?author=310674">Jay Penner</a><br><span class="torSeries">Series: <a
                        class="series" href="/tor/browse.php?series=80622">Whispers of Atlantis</a>(#5) </span><br><span
                    class="torRowDesc">historical fiction, mesopotamia</span><br><span
                    class="torFileTypes"><a>epub</a></span> | 0 comments<br>
                <div class="browseInactSeed">Previously Seeding</div>
            </td>
            <td><a class="directDownload"
                    href="/tor/download.php/EmlUBiZtUMLh5MIyJY3smWPxcZYlPYDDbQ8StIkVUjs95ENntzQ,WwVmn4OvVIpgNa8MIscKdZu7SIstIB2faIJcbswu5hWFGX7nZGt4M5TrhlcHYA9QDwerNsiWj4Q4Y+Xt6s+oGBinrfACgGOnCpRLBikifXWbu+gRUbNWGMvuHYIUbpa1cpTn"
                    title="Direct Download" alt="Direct Download"> </a></td>
            <td>
                <p>0.0 KiB</p>
                <p>741.5 KiB</p>
                <p>0.000</p>
            </td>
            <td><span title="2024-03-19 10:25:14">2024-03-19</span><br>0:00<br><span
                    title="2024-03-19 10:25:23">2024-03-19</span><br><span class="row1-darkg">32d&nbsp;01:25:13</span>
            </td>
            <td>
                <p>14</p>
                <p>0</p>
                <p>29</p>
            </td>
        </tr>
        <tr>
            <td><a class="newCatLink" href="/tor/browse.php?tor[cat][]]=63">
                    <div class="cat63">&nbsp;</div>
                </a></td>
            <td><img src="https://cdn.myanonamouse.net/pic/vip.png" alt="VIP" title="VIP"><br><img
                    alt="Contains Crude Language" title="Contains Crude Language"
                    src="https://cdn.myanonamouse.net/pic/language.png"><img alt="Contains Violence"
                    title="Contains Violence" src="https://cdn.myanonamouse.net/pic/hand.png"></td>
            <td><a href="/t/1016030" class="torTitle">Melody of Mana 5</a> by <a class="author"
                    href="/tor/browse.php?author=394962">Wandering Agent</a><br><span class="torSeries">Series: <a
                        class="series" href="/tor/browse.php?series=101361">Melody of Mana</a>(#5) </span><br><span
                    class="torRowDesc">Publisher ‏ : ‎ Podium Publishing (March 12, 2024) | Print length ‏ : ‎ 209 pages
                    | {requested}</span><br><span class="torFileTypes"><a>epub</a></span> | 0 comments<br>
                <div class="browseInactSeed">Previously Seeding</div>
            </td>
            <td><a class="directDownload"
                    href="/tor/download.php/UK9ykcCLwZ,HGoKgFFNY43KRjH6YC16uZI62P7axXfKxB9lumOqfeW8Vd03IdJJeK6BEtOCeIUCsXxK9oOrYexhD7ct0Rv6p+RoGKGlkkgUbAUg,tC5,2iNNRKQOKBDQzwQ7DVbYRkpyiaDw96gwi6WROHxxCc+OgMBz6uICOdrFzIc4y4lPMdVN"
                    title="Direct Download" alt="Direct Download"> </a></td>
            <td>
                <p>0.0 KiB</p>
                <p>1.0 MiB</p>
                <p>0.000</p>
            </td>
            <td><span title="2024-03-19 11:00:29">2024-03-19</span><br>0:00<br><span
                    title="2024-03-19 11:00:33">2024-03-19</span><br><span class="row1-darkg">32d&nbsp;02:53:05</span>
            </td>
            <td>
                <p>33</p>
                <p>0</p>
                <p>63</p>
            </td>
        </tr>
        <tr>
            <td><a class="newCatLink" href="/tor/browse.php?tor[cat][]]=75">
                    <div class="cat75">&nbsp;</div>
                </a></td>
            <td></td>
            <td><a href="/t/1015721" class="torTitle">Allen Carr's Easy Way to Quit Vaping: Get Free from JUUL, IQOS,
                    Disposables, Tanks or Any Other Nicotine Product</a> by <a class="author"
                    href="/tor/browse.php?author=15850">Allen Carr</a><a class="author"
                    href="/tor/browse.php?author=170070">John Dicey</a><br><span class="torRowDesc">selfhelp, vape,
                    vaping, smoking</span><br><span class="torFileTypes"><a>azw3</a><a>epub</a></span> | 0 comments<br>
                <div class="browseInactSeed">Previously Seeding</div>
            </td>
            <td><a class="directDownload"
                    href="/tor/download.php/OfPa9MloAK,cohDMFi7lrzXHRxfEvinH+IIDJnLc6GWpOrujRhCfh1Jmp2+3WAroGsLsP,s6i1zXorb4LvcmmRQRp+TDW3eyLXgeuyA5VW1Cgh79lAbTgtNKD99a41muUgAHd+ln,tnGKZSvC670gAFCkakFjlRaHsO8Ael5bsXtFR+LY20wywQw"
                    title="Direct Download" alt="Direct Download"> </a></td>
            <td>
                <p>0.0 KiB</p>
                <p>1.3 MiB</p>
                <p>0.000</p>
            </td>
            <td><span title="2024-03-19 10:24:28">2024-03-19</span><br>0:00<br><span
                    title="2024-03-19 10:24:36">2024-03-19</span><br><span class="row1-darkg">32d&nbsp;03:54:04</span>
            </td>
            <td>
                <p>140</p>
                <p>1</p>
                <p>230</p>
            </td>
        </tr>
        <tr>
            <td><a class="newCatLink" href="/tor/browse.php?tor[cat][]]=63">
                    <div class="cat63">&nbsp;</div>
                </a></td>
            <td><img src="https://cdn.myanonamouse.net/pic/vip.png" alt="VIP" title="VIP"><br></td>
            <td><a href="/t/1014735" class="torTitle">The Assassin's Trial</a> by <a class="author"
                    href="/tor/browse.php?author=90523">Michael Anderle</a><br><span class="torSeries">Series: <a
                        class="series" href="/tor/browse.php?series=78712">Skharr DeathEater</a>(#8) </span><br><span
                    class="torRowDesc">Fantasy &gt; Action, Adventure, Published October 2021</span><br><span
                    class="torFileTypes"><a>epub</a></span> | 0 comments<br>
                <div class="browseInactSeed">Previously Seeding</div>
            </td>
            <td><a class="directDownload"
                    href="/tor/download.php/C+w4jvZVwf6zmCb4jpV4TlHeHxD3oPXzZAOD5NR8iuIRKSmTLPflDzBa8qJHPkgYUMD401MgQy4F8Cme5A+EA6lQc+EnY,yAqI,en,TaeNXyySchi9RpVZeYsBgdaPm5N730Kj1AilQ1LlwT8Ply72AjlyyUzBDahqHoRfod9896wqS1mGNOAVqN"
                    title="Direct Download" alt="Direct Download"> </a></td>
            <td>
                <p>0.0 KiB</p>
                <p>446.6 KiB</p>
                <p>0.000</p>
            </td>
            <td><span title="2024-03-14 04:40:32">2024-03-14</span><br>0:00<br><span
                    title="2024-03-14 04:40:36">2024-03-14</span><br><span class="row1-darkg">35d&nbsp;00:26:09</span>
            </td>
            <td>
                <p>29</p>
                <p>0</p>
                <p>50</p>
            </td>
        </tr>
        <tr>
            <td><a class="newCatLink" href="/tor/browse.php?tor[cat][]]=94">
                    <div class="cat94">&nbsp;</div>
                </a></td>
            <td></td>
            <td><a href="/t/1014599" class="torTitle">Chillin' Out</a> by <a class="author"
                    href="/tor/browse.php?author=68922">Patti Benning</a><br><span class="torSeries">Series: <a
                        class="series" href="/tor/browse.php?series=114795">Real Estate Rescue</a>(#14) </span><br><span
                    class="torRowDesc">Publication Date: March 7, 2024, Print Length: 85 pages</span><br><span
                    class="torFileTypes"><a>epub</a></span> | 0 comments<br>
                <div class="browseInactSeed">Previously Seeding</div>
            </td>
            <td><a class="directDownload"
                    href="/tor/download.php/pOi04yDXNs9kPOh5nerVsKENmjQDdVS7+J7LYwFoGYiB5+Q6+ftDfdbFl7t72,2Gckp2hx8oA2J0QxfsFApqNT+ehPUWYE55NBypaWXmXVBzjNiARpfePYCaxhn3Qp6FIXneBUqq,LsNynXncqaB0lcVm4PmHgil7Jl65PSU5UG8tAYC6kZhrumL"
                    title="Direct Download" alt="Direct Download"> </a></td>
            <td>
                <p>0.0 KiB</p>
                <p>895.6 KiB</p>
                <p>0.000</p>
            </td>
            <td><span title="2024-03-14 04:40:21">2024-03-14</span><br>0:00<br><span
                    title="2024-03-14 04:40:24">2024-03-14</span><br><span class="row1-darkg">35d&nbsp;05:08:54</span>
            </td>
            <td>
                <p>21</p>
                <p>0</p>
                <p>37</p>
            </td>
        </tr>
    </tbody>
</table>
"""

soup = BeautifulSoup(html_table, 'html.parser')

rows = soup.find_all('tr')

href_values = []

for row in rows:
    cols = row.find_all('td')
    if len(cols) >= 3:
        img_tag = cols[1].find('img', title = 'VIP')
        if img_tag:
            a_tag = cols[2].find('a')
            if a_tag:
                href_value = a_tag['href']
                href_values.append('https://www.myanonamouse.net'+href_value)
            
print("VIP href values: ", href_values)

for url in href_values:
    try:
        response = urllib.request.urlopen(url)
        content  = response.read().decode('utf-8')
        print(f"Content from {url}:\n{content}\n")
    except Exception as e:
        print(f"Error fetching {url}: {e}")