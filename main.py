from googlesearch import search 
from weasyprint import HTML
import argparse
import sys
import xmltodict 
import requests

test_xml_data = """<?xml version="1.0" encoding="UTF-8"?><rss xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:content="http://purl.org/rss/1.0/modules/content/" xmlns:atom="http://www.w3.org/2005/Atom" version="2.0" xmlns:cc="http://cyber.law.harvard.edu/rss/creativeCommonsRssModule.html">
    <channel>
        <title><![CDATA[Stories by Aneeta Sharma on Medium]]></title>
        <description><![CDATA[Stories by Aneeta Sharma on Medium]]></description>
        <link>https://medium.com/@anaida07?source=rss-2d7c94064f84------2</link>
        <image>
            <url>https://cdn-images-1.medium.com/fit/c/150/150/1*MD5-_hwdb2S9aLnWW6YyNA.jpeg</url>
            <title>Stories by Aneeta Sharma on Medium</title>
            <link>https://medium.com/@anaida07?source=rss-2d7c94064f84------2</link>
        </image>
        <generator>Medium</generator>
        <lastBuildDate>Tue, 12 May 2020 15:31:26 GMT</lastBuildDate>
        <atom:link href="https://medium.com/feed/@anaida07" rel="self" type="application/rss+xml"/>
        <webMaster><![CDATA[yourfriends@medium.com]]></webMaster>
        <atom:link href="http://medium.superfeedr.com" rel="hub"/>
        <item>
            <title><![CDATA[Inside the book — Full-Stack Web Development with Vue.js and Node]]></title>
            <link>https://codeburst.io/inside-the-book-full-stack-web-development-with-vue-js-and-node-50638d4dcc6a?source=rss-2d7c94064f84------2</link>
            <guid isPermaLink="false">https://medium.com/p/50638d4dcc6a</guid>
            <category><![CDATA[javascript]]></category>
            <category><![CDATA[vuejs]]></category>
            <category><![CDATA[nodejs]]></category>
            <category><![CDATA[expressjs]]></category>
            <category><![CDATA[software-development]]></category>
            <dc:creator><![CDATA[Aneeta Sharma]]></dc:creator>
            <pubDate>Wed, 16 May 2018 07:48:22 GMT</pubDate>
            <atom:updated>2018-05-29T12:58:04.649Z</atom:updated>
            <content:encoded><![CDATA[<figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*kZnwcP48e4CWMHEaE2oG7A.png" /><figcaption>Full-Stack Web Development with Vue.js and Node</figcaption></figure><p>Finally, after a long awaited time, the book is here. I just completed writing a book, <strong>Full Stack Web Development with Vue.js and Node</strong> which talks about how we can build web applications using the technologies in MEVN stack i.e. (MongoDB, Express.js, Vue.js and Node.js). More details on the book can be found here(<a href="https://www.packtpub.com/web-development/full-stack-web-development-vuejs-and-node">https://www.packtpub.com/web-development/full-stack-web-development-vuejs-and-node</a>) in Packt Publishing.</p><p>If you are a web developer and want to try hands on building web applications learning just one programming language i.e. JavaScript, then this book is for you.</p><p>The book guides you through the technology stack called <strong>MEVN</strong> which just replaces the frontend layer of <a href="https://angularjs.org/">Angular.js</a> from MEAN or <a href="https://reactjs.org/">React.js</a> from MERN and introduces <a href="https://vuejs.org/">Vue.js</a>.</p><p>This book guides you through building a web application with Express.js which is a Node.js framework followed by adding the database layer with MongoDB and then the frontend layer with Vue.js to create a robust application.</p><h3>Who the book is for?</h3><p>This book is suitable for people who have the basic understanding of the following things:</p><ul><li>Knowledge of HTML, CSS and JavaScript</li><li>Knowledge of MVC architecture</li><li>Knowledge of <a href="http://meanjs.org/">MEAN</a> and <a href="http://mern.io/">MERN</a> stacks is the cherry to the cake</li></ul><h3>Key takeaways from this book:</h3><ul><li>Learn to install Node.js and other software packages required to build a full application</li><li>Build an application using Express.js</li><li>Create Schemas using Mongoose</li><li>Build RESTful APIs using Express.js</li><li>Build a Single Page Application using Vue.js and Express.js</li><li>Learn to leverage Vuex to build complex applications</li><li>Add test cases to improve the reliability of the application</li><li>Add authorization using passport.js and learn about several Oauth Strategies that passport.js provides</li><li>Learn how to deploy apps on Heroku using Github</li></ul><h3>Sneak peek of the application</h3><p>Throughout the book, we will be building a movie rating application with the following features:</p><ul><li>A home page that lists all the movies</li></ul><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*2cHf-ClESPSTawQAP33JeA.png" /><figcaption>Movies Listing Page</figcaption></figure><ul><li>Ability to add movies</li></ul><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*fEXQMCBn6MxHaOYgCO3oWQ.png" /><figcaption>Add Movie Page</figcaption></figure><ul><li>Ability for users to sign up and sign in — using both local authentication along with several OAuth Strategies</li></ul><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*8kX23VRE6Jhg7TvwhJEK2g.png" /><figcaption>User sign in page</figcaption></figure><ul><li>The user will be able to rate a movie</li></ul><figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*ucXKQJU8HKowCqTSbQgHMg.png" /><figcaption>Rate movie page</figcaption></figure><h3>Start Reading the Book</h3><p>You can grab yourself a copy from Amazon from the following link:<a href="https://www.amazon.co.uk/Full-Stack-Web-Development-Vue-js-Node/dp/1788831144/ref=sr_1_1?s=books&amp;ie=UTF8&amp;qid=1526455991&amp;sr=1-1&amp;keywords=aneeta+sharma"> Full-Stack Web Development with Vue.js and Node</a></p><p>Also, there is a launch discount as well for the ebook version which you can get from Packt Publishing here: <a href="https://www.packtpub.com/web-development/full-stack-web-development-vuejs-and-node">https://www.packtpub.com/web-development/full-stack-web-development-vuejs-and-node</a></p><figure><a href="http://bit.ly/codeburst"><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*i3hPOj27LTt0ZPn5TQuhZg.png" /></a></figure><blockquote>✉️ <em>Subscribe to </em>CodeBurst’s<em> once-weekly </em><a href="http://bit.ly/codeburst-email"><strong><em>Email Blast</em></strong></a><strong><em>, </em></strong>🐦 <em>Follow </em>CodeBurst<em> on </em><a href="http://bit.ly/codeburst-twitter"><strong><em>Twitter</em></strong></a><em>, view </em>🗺️ <a href="http://bit.ly/2018-web-dev-roadmap"><strong><em>The 2018 Web Developer Roadmap</em></strong></a><em>, and </em>🕸️ <a href="http://bit.ly/learn-web-dev-codeburst"><strong><em>Learn Full Stack Web Development</em></strong></a><em>.</em></blockquote><img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=50638d4dcc6a" width="1" height="1"><hr><p><a href="https://codeburst.io/inside-the-book-full-stack-web-development-with-vue-js-and-node-50638d4dcc6a">Inside the book — Full-Stack Web Development with Vue.js and Node</a> was originally published in <a href="https://codeburst.io">codeburst</a> on Medium, where people are continuing the conversation by highlighting and responding to this story.</p>]]></content:encoded>
        </item>
        <item>
            <title><![CDATA[Build full stack web apps with MEVN Stack [Part 2/2]]]></title>
            <description><![CDATA[<div class="medium-feed-item"><p class="medium-feed-image"><a href="https://medium.com/@anaida07/mevn-stack-application-part-2-2-9ebcf8a22753?source=rss-2d7c94064f84------2"><img src="https://cdn-images-1.medium.com/max/600/1*TjRR2msP6G116cSOr_96VA.png" width="600"></a></p><p class="medium-feed-snippet">[Update] I have written a book(Full-Stack Web Development with Vue.js and Node) which talks about how we can build web applications using&#x2026;</p><p class="medium-feed-link"><a href="https://medium.com/@anaida07/mevn-stack-application-part-2-2-9ebcf8a22753?source=rss-2d7c94064f84------2">Continue reading on Medium »</a></p></div>]]></description>
            <link>https://medium.com/@anaida07/mevn-stack-application-part-2-2-9ebcf8a22753?source=rss-2d7c94064f84------2</link>
            <guid isPermaLink="false">https://medium.com/p/9ebcf8a22753</guid>
            <category><![CDATA[full-stack]]></category>
            <category><![CDATA[software-engineering]]></category>
            <category><![CDATA[expressjs]]></category>
            <category><![CDATA[vuejs]]></category>
            <category><![CDATA[javascript]]></category>
            <dc:creator><![CDATA[Aneeta Sharma]]></dc:creator>
            <pubDate>Wed, 20 Sep 2017 17:54:39 GMT</pubDate>
            <atom:updated>2018-06-02T04:48:57.266Z</atom:updated>
        </item>
        <item>
            <title><![CDATA[Build full stack web apps with MEVN Stack [Part 1/2]]]></title>
            <description><![CDATA[<div class="medium-feed-item"><p class="medium-feed-image"><a href="https://medium.com/@anaida07/mevn-stack-application-part-1-3a27b61dcae0?source=rss-2d7c94064f84------2"><img src="https://cdn-images-1.medium.com/max/1664/1*JUDEODxwUNsxmiAKUDKkRg.png" width="1664"></a></p><p class="medium-feed-snippet">[Update] I have written a book(Full-Stack Web Development with Vue.js and Node) which talks about how we can build web applications using&#x2026;</p><p class="medium-feed-link"><a href="https://medium.com/@anaida07/mevn-stack-application-part-1-3a27b61dcae0?source=rss-2d7c94064f84------2">Continue reading on Medium »</a></p></div>]]></description>
            <link>https://medium.com/@anaida07/mevn-stack-application-part-1-3a27b61dcae0?source=rss-2d7c94064f84------2</link>
            <guid isPermaLink="false">https://medium.com/p/3a27b61dcae0</guid>
            <category><![CDATA[javascript]]></category>
            <category><![CDATA[software-engineering]]></category>
            <category><![CDATA[vuejs]]></category>
            <category><![CDATA[full-stack]]></category>
            <category><![CDATA[expressjs]]></category>
            <dc:creator><![CDATA[Aneeta Sharma]]></dc:creator>
            <pubDate>Mon, 18 Sep 2017 09:16:35 GMT</pubDate>
            <atom:updated>2018-06-02T04:46:23.563Z</atom:updated>
        </item>
        <item>
            <title><![CDATA[Running Rubocop Only On Modified Files]]></title>
            <link>https://medium.com/devnetwork/running-rubocop-only-on-modified-files-a21aed86e06d?source=rss-2d7c94064f84------2</link>
            <guid isPermaLink="false">https://medium.com/p/a21aed86e06d</guid>
            <category><![CDATA[rubocop]]></category>
            <category><![CDATA[software-engineering]]></category>
            <category><![CDATA[refactoring]]></category>
            <category><![CDATA[git]]></category>
            <category><![CDATA[github]]></category>
            <dc:creator><![CDATA[Aneeta Sharma]]></dc:creator>
            <pubDate>Thu, 20 Apr 2017 16:44:34 GMT</pubDate>
            <atom:updated>2017-11-29T08:03:48.051Z</atom:updated>
            <content:encoded><![CDATA[<figure><img alt="" src="https://cdn-images-1.medium.com/max/400/1*aAQWjUDVdMJeU_on2rUnVg.jpeg" /></figure><p>If you are using <a href="http://batsov.com/rubocop/"><strong>Rubocop</strong></a><strong> </strong>as a code analyzer and following its guidelines as a standard for your project, then like me you also might have faced the annoyance of running Rubocop on each and every modified file individually. Its boring and a little time consuming as well. Hence, its lot more productive to run it only on the updated files and for once.</p><p>There are two ways to run Rubocop on modified files:</p><p><strong>[1] Before committing<br></strong>To view the list of files that have been modified, you can do:</p><pre>git ls-files -m</pre><p>This lists all the modified files regardless of the extensions as well as the deleted files. To exclude deleted files you can do:</p><pre>git ls-files -m | xargs ls -1 2&gt;/dev/null</pre><p>Again, if you wish to view only the modified files with .rb extension, you can do:</p><pre>git ls-files -m | xargs ls -1 2&gt;/dev/null | grep &#39;\.rb$&#39;</pre><p>Hence, the final command to run Rubocop for modified files is:</p><pre>git ls-files -m | xargs ls -1 2&gt;/dev/null | grep &#39;\.rb$&#39; | xargs rubocop</pre><p><strong>[2] After committing<br></strong>There are two ways to view the list of changed files after you have committed. First is to compare the changes with master or you can compare it with the current upstream.</p><p>To compare with master:</p><pre>git diff-tree -r --no-commit-id --name-only head origin/master</pre><p>To compare with current upstream:</p><pre>git diff-tree -r --no-commit-id --name-only @\{u\} head</pre><p><em>Note: This won’t work if you haven’t yet set up a remote branch.</em></p><p>Hence, the file command to run Rubocop for modified files is:</p><pre>git diff-tree -r --no-commit-id --name-only head origin/master | xargs rubocop</pre><p>or</p><pre>git diff-tree -r --no-commit-id --name-only @\{u\} head | xargs rubocop</pre><p>With this, you will be saving quite a time. To top if off, you can also create aliases for these.</p><img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=a21aed86e06d" width="1" height="1"><hr><p><a href="https://medium.com/devnetwork/running-rubocop-only-on-modified-files-a21aed86e06d">Running Rubocop Only On Modified Files</a> was originally published in <a href="https://medium.com/devnetwork">Devnetwork</a> on Medium, where people are continuing the conversation by highlighting and responding to this story.</p>]]></content:encoded>
        </item>
        <item>
            <title><![CDATA[Importance of Soft Skills for Software Engineers]]></title>
            <link>https://medium.com/@anaida07/importance-of-soft-skills-for-software-engineers-7965be2074dc?source=rss-2d7c94064f84------2</link>
            <guid isPermaLink="false">https://medium.com/p/7965be2074dc</guid>
            <category><![CDATA[soft-skills]]></category>
            <category><![CDATA[software-engineer]]></category>
            <category><![CDATA[education]]></category>
            <category><![CDATA[careers]]></category>
            <dc:creator><![CDATA[Aneeta Sharma]]></dc:creator>
            <pubDate>Mon, 17 Apr 2017 17:06:05 GMT</pubDate>
            <atom:updated>2017-04-17T17:06:05.855Z</atom:updated>
            <content:encoded><![CDATA[<figure><img alt="" src="https://cdn-images-1.medium.com/max/600/1*dI7nobGRZOmxKJ7T4wu4GQ.jpeg" /></figure><p>Typically as a software engineer, all we think and care about is coding. We assume having the technical expertise is sufficient to execute our job duties. But little do we know that having the technical skills is only one of the many facets of being an effective person in the work place. The major one being ‘<strong>Soft Skills</strong>’.</p><p>Simply put, Soft Skills are the interpersonal personality traits which allows us to collaborate with others and interact with others effectively. Soft Skills enhances our ability to become a good speaker as well as a good listener. It not only helps to work more productively, but also helps to establish ourselves as a better person. Hence, this is an investment worth making.</p><p>The importance of <strong>soft skills</strong> is often underestimated but these are what accompany the hard skills. Like all skills, these can also be learned. The best thing about soft skills is you don’t need any qualifications to acquire them and you can start working on them right now.</p><p>Some of the most common soft skills include:</p><ol><li><strong>Clarity of communication</strong></li><li><strong>Degree of collaboration / Teamwork</strong></li><li><strong>Conflict Resolution</strong></li><li><strong>Inclusion</strong></li><li><strong>Coaching / Mentoring</strong></li></ol><blockquote>When it comes to soft skills, show — don’t tell.</blockquote><p>Soft skills are becoming the hard skills in this fast changing world. It’s not enough to be highly skilled in technical field without developing skills that helps to collaborate and communicate with people effectively. These all have a significant impact on a person’s attitude which ultimately ties back to success.</p><p>The list is not exhaustive but working towards any of these will definitely pay off in one’s career and in life more generally.</p><img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=7965be2074dc" width="1" height="1">]]></content:encoded>
        </item>
        <item>
            <title><![CDATA[How Reading Can Transform Your Life]]></title>
            <link>https://medium.com/@anaida07/how-reading-can-transform-your-life-5f9298ce9f6c?source=rss-2d7c94064f84------2</link>
            <guid isPermaLink="false">https://medium.com/p/5f9298ce9f6c</guid>
            <category><![CDATA[books]]></category>
            <category><![CDATA[reading]]></category>
            <dc:creator><![CDATA[Aneeta Sharma]]></dc:creator>
            <pubDate>Sun, 16 Apr 2017 15:43:30 GMT</pubDate>
            <atom:updated>2019-09-12T18:11:55.377Z</atom:updated>
            <content:encoded><![CDATA[<figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*psu7kH8_Is9RzKsN00RrUQ.jpeg" /></figure><blockquote>Reading is to the mind what exercise is to your body.</blockquote><p>Recently I have been on a series of reading, getting my hands on anything I find. No matter what I read, there’s always something new to learn. From a non reader to becoming a reader, it has shown me how a simple act of reading can help improve the various aspects of our life. To name a few, here’s how one can benefit when you crack open a book:</p><p><strong>Stress Reduction<br></strong>No matter how much stressed you are at work or in your personal life, reading can easily melt away that stress by distraction. It transports you to another world where you don’t think about the hardships of day to day life.<br>Reading puts you into a good mood.</p><p><strong>Tranquility<br></strong>Reading can bring immense inner peace. It brings an inner state of being calm. The concentration you put while reading soothes and helps remove anxiety.</p><p><strong>Increased Vocabulary<br></strong>Reading is a workout to your brain. Whether you are scanning the book or deeply concentrating on it, you are feeding your brain something new. You can always read books to expand your mental dictionary.</p><blockquote>A <strong>reader</strong> lives a thousand lives before he dies. The man who never reads lives only one.</blockquote><p>Reading encourages positive thinking, improves empathy, improves concentration and keeps the brain young. When you start to read more, you will discover more reasons to stick with it.</p><p><em>Want to find out more reasons? Why not grab a book and start reading ;)</em></p><img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=5f9298ce9f6c" width="1" height="1">]]></content:encoded>
        </item>
        <item>
            <title><![CDATA[We Are More]]></title>
            <link>https://medium.com/@anaida07/we-are-more-c77dccd2e44a?source=rss-2d7c94064f84------2</link>
            <guid isPermaLink="false">https://medium.com/p/c77dccd2e44a</guid>
            <category><![CDATA[women-in-tech]]></category>
            <category><![CDATA[leadership]]></category>
            <category><![CDATA[self-confidence]]></category>
            <category><![CDATA[tech]]></category>
            <dc:creator><![CDATA[Aneeta Sharma]]></dc:creator>
            <pubDate>Fri, 14 Apr 2017 04:23:20 GMT</pubDate>
            <atom:updated>2017-04-14T04:23:20.832Z</atom:updated>
            <content:encoded><![CDATA[<figure><img alt="" src="https://cdn-images-1.medium.com/max/1024/1*878o0x3Utxajo94Hp6habA.jpeg" /></figure><p>It goes without saying that Women in Technology is growing day by day and the community is flourishing. Most women today are as aware of and addicted to technology as men are. Many women are taking up technology as their field of career and research. But despite of this development, there is a destitution due to which the spike is not there. There are so few females who hold leadership positions throughout the globe. In Nepal, its even less. Though there is an elevated growth, it’s not enough to catch up with the progress made in the field in other countries.</p><blockquote>There is still a big gap between the number of men and women in the workplace, particularly further up the leadership ladder owning to the confidence issues concerning the aptitude. We have an abundance of talented women techmakers with us but they need to come out of their cocoons and interact more to sell themselves in the market.</blockquote><p>Here are some points which can help to move forward in that direction:</p><h3><strong>1. Seek opportunities</strong></h3><p>Many tech organizations around the world are always in search of fresh talents. The demand for skilled techmakers is at an all-time high. For a head start, brainstorming sessions, workshops, meetups and tech centered events are of a great help. There are countless of opportunities out there already. Grab them and use it to the maximum advantage.</p><h3><strong>2. Get out of comfort zone</strong></h3><p>Set goals for yourself. Make a list of the things and add deadlines. The main point is to challenge yourself. Start small but think big. And make sure to reflect on that once you make it happen. Figure out what went well, what didn’t and what is there to improve further. You can also make it interesting by giving yourself a treat when you cross off a task from your checklist :P</p><h3>3. SpeakUp</h3><p>Interaction is the key to success. Build networks and surround yourself with people who can help you grow. Search for mentors. Speak up and ask for help when it’s needed and advocate when required. And always share what you learn. Spread your wisdom :)</p><img src="https://medium.com/_/stat?event=post.clientViewed&referrerSource=full_rss&postId=c77dccd2e44a" width="1" height="1">]]></content:encoded>
        </item>
    </channel>
</rss>"""

parser = argparse.ArgumentParser(description='Search Medium for a desired topic and save the top results in pdf format')
parser.add_argument('term', help="search term to use", nargs='+')

args = parser.parse_args()
term = " ".join(args.term)

# TODO: search term and get list of results :DONE
# TODO: take results, filter users and get xss feed of articles from medium :DONE
# TODO: filter articles by post and get content :DONE
# TODO: convert the content html or pdf :DONE
# TODO: worry about formatting
# TODO: accept path to store pdf files and number of files to download

query = f'site:medium.com {term}'

search_results = list(search(query, num=1, start=0, stop=5))

for result in search_results:
  userid = result.split('/')[3]
  post_slug = result.split('/')[4]
  feed_url = f"https://medium.com/feed/{userid}/"

  response = requests.get(feed_url)  
  xml_data = response.text

  rss_data = xmltodict.parse(xml_data)
  items_by_user = rss_data['rss']['channel']['item']

  for item in items_by_user:
    link = item['link']
    if 'content:encoded' in item and post_slug in link:
      content = item['content:encoded']
      filename = "-".join(link.split('?')[0].split('/')[-1].split('-')[:-1])+'.pdf'

      HTML(string=content).write_pdf('./'+filename)
print("[+] All Done ;)")