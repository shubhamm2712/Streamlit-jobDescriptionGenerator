import streamlit as st
import sqlite3

@st.cache
def write_about_company(name):
    a=[]
    for text in company:
        a.append(text.replace('_*COMPANY*_',name))
    return a

@st.cache 
def find_role_des(role,name):
    a="<ol>"
    for text in role_description[role]:
        a+="<li>"+(text.replace('_*COMPANY*_',name))+"</li>"
    a+="</ol>"
    return a

@st.cache 
def find_role_req(role,name):
    a="<ol>"
    for text in role_requirement[role]:
        a+="<li>"+(text.replace('_*COMPANY*_',name))+"</li>"
    a+="</ol>"
    return a

@st.cache 
def find_bpoints(role,name):
    a="<ol>"
    for text in brownie_points[role]:
        a+="<li>"+(text.replace('_*COMPANY*_',name))+"</li>"
    a+="</ol>"
    return a

@st.cache 
def find_perks(role,name):
    a="<ol>"
    for text in perks:
        a+="<li>"+(text.replace('_*COMPANY*_',name))+"</li>"
    a+="</ol>"
    return a

@st.cache 
def find_tstack(role,name):
    a=[]
    for text in tech_stack:
        a.append(text.replace('_*COMPANY*_',name))
    return a

@st.cache 
def find_afterapp(role,name):
    a="<ol><li>"+(after_application[0].replace('_*COMPANY*_',name))+"</li><li>"+after_application[1]+"<ul>"
    a+="<li>"+after_application[2][0]+"</li><li>"+after_application[2][1]+"</li><li>"+after_application[2][2]+"</li></ul></ol>"
    return a

roles=['Product Manager','Frontend Engineer','Backend Engineer','Software Engineer','Fullstack Engineer','Product Engineer','Head of Engineering','QA Engineer','Android Engineer','iOS Engineer','DevOps Engineer','Data Scientist'] 
company = ["_*COMPANY*_ helps companies automate the first round technical interview screening with a conversational chatbot, Ada. We're currently working with governments, banks, tech giants, Fortune 500 staffing companies and tech startups to help streamline their recruitment processes.","_*COMPANY*_ is headquartered in Singapore with an office in Bengaluru, India."]
role_description = {
    'Product Manager':["Grow _*COMPANY*_'s SaaS offering by understanding and solving our customers problems. You will deliver world-class experiences and change how our customers hire engineers.","Develop a deep understanding of our customers problems and work with a team of excellent engineers and designers to solve them.","Help define the goals and vision for the _*COMPANY*_ to help some of the largest companies in the world recruit engineers, while developing and delivering a roadmap of impactful features and helping the team develop and measure KPIs for success.","Work across different teams to deliver solutions merging many teams offerings, and bringing features to customers in different industries."],
    'Frontend Engineer':["Lead parts of the product from inception to launch, and own large parts of the product’s execution.","Architect new features and reusable UI paradigms using ReactJS with the goal of delighting and increasing the success of our users.","Contribute to the development of the product while working with a cross-functional team of product managers, designers, and engineers.","Contribute to building features using design and API mocks and write contracts, integration & unit tests for features built.","Perform peer code reviews."],
    'Backend Engineer':["Leading parts of the product from inception to launch, and own large parts of the product’s execution.","Working with our product management and frontend team to build products with the goal of delighting and increasing the success of our users.","Deploying machine learning algorithms and augmenting data scientists to make our AI platform smarter","Architecting, building, testing, and releasing product-facing features.","Contributing to our side projects and free tools for the recruitment industry."],
    'Software Engineer':["Leading parts of the product from inception to launch, and own large parts of the product’s execution.","Working with our product management and frontend team to build products with the goal of delighting and increasing the success of our users.","Deploying machine learning algorithms and augmenting data scientists to make our AI platform smarter","Architecting, building, testing, and releasing product-facing features.","Contributing to our side projects and free tools for the recruitment industry."],
    'Fullstack Engineer':["Leading parts of the product from inception to launch, and own large parts of the product’s execution.","Working with our product management and frontend team to build products with the goal of delighting and increasing the success of our users.","Deploying machine learning algorithms and augmenting data scientists to make our AI platform smarter","Architecting, building, testing, and releasing product-facing features.","Contributing to our side projects and free tools for the recruitment industry."],
    'Product Engineer':["Leading parts of the product from inception to launch, and own large parts of the product’s execution.","Working with our product management and frontend team to build products with the goal of delighting and increasing the success of our users.","Deploying machine learning algorithms and augmenting data scientists to make our AI platform smarter","Architecting, building, testing, and releasing product-facing features.","Contributing to our side projects and free tools for the recruitment industry.","Grow your team’s capacity by mentoring other engineers and interviewing candidates. This is a chance to be an integral part of building and growing a team."],
    'Head of Engineering':["Manage a team of backend and frontend engineers in one or more product areas. You will initially manage up to 15 engineers, partner with the product owners of multiple areas of the platform from an engineering perspective, help define the product roadmap and deliver a high quality product.","Collaborate with PMs to define roadmap for your area of the product","Master our existing infrastructure, but question everything and offer suggestions on how we can improve","You will be responsible for the overall performance and management of the engineering team including reporting and mentoring, and also hiring and growing the team.","Help scale to thousands of customers. We need great engineers constantly improving our tech and peering round the corner."],
    'QA Engineer':["You will owning features through inception, design feedback, implementation, and launch. This will include building test plans for new features and improvising on existing test plans for feature updates and customer feedback.","You will collaborating with Product Designers, Product Managers, Backend Engineers, Data Engineers and Customer Support","You will identify areas for automation and writing automated tests to ensure repeatability, coverage, reliability and catching regressions."],
    'Android Engineer':["Collaborate with all dev teams to build new features and their integration with back-end services while maintaining existing features and being a force of proposition for architecture improvements.","Build robust, maintainable code to support a rapidly evolving product.","Work closely with Product and Design teams to drive product direction.","Design lightweight mobile APIs.","Explore and advocate for the latest architectural trends in order to keep Tally android technology innovative and relevant.","Develop with testing in mind and leverage testing frameworks in order to produce consistent, high-quality features.","Understand product requirements beyond the written word and take pride in crafting intuitive and delightful experiences on mobile."],
    'iOS Engineer':["Using Objective-C and Swift along with XCode and CocoaPods, you'll be maintaining and evolving the software for current and future needs in order to develop highly innovative, consumer-facing mobile products, while supporting the product roadmap","Building new features, refactoring code, and tweaking existing features based on our users needs","Designing, developing, testing, deploying, maintaining, and enhancing elegant mobile solutions","Working directly with quality engineers to identify test cases and devise efficient, scalable testing processes to allow us to run weekly to monthly releases","Communicating with the leadership team, product managers, and other engineers on business and technical priorities"],
    'DevOps Engineer':["You will work towards architecting robust RESTful services to collect and provide data on potential customers.","You will craft highly efficient, customized campaigns to automate outreach.","You will work closely with Data Science and Operations to gather business intelligence firm-wide and make recommendations to improve the entire company.","You will be responsible for operating and maintaining enterprise-scale databases and external integrations."],
    'Data Scientist':["Mining text data for use in classification / predicting business outcomes.","Building anomaly detection models to determine fraudulent activity, unexpected trends in data, etc.","Applying machine learning to image classification for key business applications.","Identifying, evaluating, and productionizing new data sources (e.g. geospatial data, web scraping, cell phone sensors).","Predictive modeling related to improving insurance pricing."]
}
role_requirement = {
    'Product Manager':["You have previous Product Management experience and a proven track record of being able to deliver highly ambitious products. You’ll be ready to show what these are, and how you made it happen. You also need to demonstrate the ability to move metrics and reach your KPI goals.","You place customers first. You make no compromise on this.","You inspire others: You can explain the customer problems clearly and include others in the team to discuss solutions. You have an ability to work with a team to develop an inspiring product vision of how you see our product developing.","You strive to be the best: Self-driven and make things happen, show a strong desire to succeed, always looking for opportunities, determined in pursuit of your own and your customers' goals.","You’re a great communicator: An effective communicator, you’re straight up and honest. You can adapt your communication style to different audiences. You’re able to persuade others and you aren’t afraid to challenge something when you need to.","You are data-driven. You need to be able to prioritise the value you can add to customers, and get the entire company behind you. Numbers are the best way to do this. You are very rigorous about measuring impact and assessing expected impact. You know how to dissociate a bad MVP from a good one and can tell the difference between an A/B test that adds value and a one that is useless.","You have deep technical know-how. You may have started out your career as an engineer or maybe it's a secret passion. You need to be able to communicate effectively with our product engineers."],
    'Frontend Engineer':["You have ~2 years of experience building applications using modern UI frameworks such as React.js. You have a deep understanding of functional and reactive programming paradigms","You probably have an eye for well functioning user interfaces, and have at least cursory insight into both design and UX principles.","You have a knack for understanding the user flows and building them out. You also have great design intuition and user empathy.","You have deep interest about the technical stack you work on to understand it better and build out responsive products.","You have familiarity with popular JavaScript tools, frameworks and design principles, and enjoy staying up to date with the changing JavaScript ecosystem landscape.","You have strong communication skills."],
    'Backend Engineer':["3+ years of industry experience in a software engineering role, preferably building a SaaS product. You can demonstrate significant impact that your work has had on the product and/or the team.","Deep knowledge of a high-level programming language (for example, Ruby, Python, Perl etc.) but it doesn’t need to be a language that we use here! Great people are effective and learn what we use quickly (or introduce us to better ways of working)","Experience with scalable distributed systems, both built from scratch as well as on AWS primitives","Willingness to learn and use new technologies.","Extremely data-driven.","Ability to debug complex systems."],
    'Software Engineer':["3+ years of industry experience in a software engineering role, preferably building a SaaS product. You can demonstrate significant impact that your work has had on the product and/or the team.","Deep knowledge of a high-level programming language (for example, Ruby, Python, Perl etc.) but it doesn’t need to be a language that we use here! Great people are effective and learn what we use quickly (or introduce us to better ways of working)","Experience with scalable distributed systems, both built from scratch as well as on AWS primitives","Willingness to learn and use new technologies.","Extremely data-driven.","Ability to debug complex systems."],
    'Fullstack Engineer':["3+ years of industry experience in a software engineering role, preferably building a SaaS product. You can demonstrate significant impact that your work has had on the product and/or the team.","Deep knowledge of a high-level programming language (for example, Ruby, Python, Perl etc.) but it doesn’t need to be a language that we use here! Great people are effective and learn what we use quickly (or introduce us to better ways of working)","Experience with scalable distributed systems, both built from scratch as well as on AWS primitives","Willingness to learn and use new technologies.","Extremely data-driven.","Ability to debug complex systems."],
    'Product Engineer':["You have 3+ years of industry experience in a software engineering role, preferably building a SaaS product. You can demonstrate significant impact that your work has had on the product and/or the team.","You have deep knowledge of a high-level programming language (Ruby, Python, Perl etc.) but it doesn’t need to be a language that we use here! Great people are effective and learn what we use quickly (or introduce us to better ways of working)","You have experience collaborating directly with product teams and designers, and a proven track record of delivering value to customers or users.","You have experience with Distributed systems."],
    'Head of Engineering':["Bachelor's degree in Computer Science, Engineering or related field, or equivalent training, fellowship, or work experience.","We're looking for someone who has a strong background as an individual contributor engineer and is now passionate about building teams and people management.","You have 5+ years of engineering management experience leading productive, high functioning teams. You can describe why these teams were high functioning and what you specifically did to ensure engineers felt productive.","You are a very strong verbal and nonverbal communicator. You’re excited to explain complex technical concepts and share your knowledge with diverse audiences both internally and externally. You can reduce complex problems to simple solutions consistently.","You can contemplate several, and often conflicting, constraints and make rapid decisions.","You can anticipate future technical needs for the product and craft plans to realize them.","You excel at building roadmaps and can develop a long-term team vision in partnership with other engineering teams at Slack. You can then be accountable for driving project execution.","You love helping engineers develop new skills and advance in their careers. You don’t shy away from performance conversations and you recognize the relationship between objective feedback and career growth."],
    'QA Engineer':["Strong quality sense and experience working closely with web development teams","Excellent communication skills and passion for tough technical problems","Attention to detail and voice of customer experience","Experience automating end to end UI tests for mobile and web apps","Experience in championing customer feedback post-launch and bringing it to the attention of relevant teams","Bachelor's degree in Computer Science, Engineering or a related field or equivalent training, fellowship, or work experience"],
    'Android Engineer':["You're intimately familiar with the lifecycle intricacies of Android components.","You have strong design intuition and user empathy.","You stay on top of Android news including new open-source libraries and best practices.","You love writing custom Views, ViewGroups, and new UX interactions.","You actively write unit tests for new code.","You write highly performant code and know how to performance tune Android apps.","You're self-driven to improve the app and codebase above and beyond what's outlined in the spec."],
    'iOS Engineer':["Strong product sense and experience working closely with Product Designers","Deep understanding of UIKit","Excellent communication skills and passion for tough technical problems","Bachelor's degree in Computer Science, Engineering or related field or equivalent training, fellowship, or work experience"],
    'DevOps Engineer':["Has a track record of building strong relationships with both internal and external business teams","Ability to communicate easily and effectively with internal and key partners’ cross-functional teams, including but not limited to: senior management, business development, marketing, product and project management, architect, engineering, operations, SC&L etc","Passionate about building bridges between our customer and our Enjoy partners; equally passionate about building bridges between systems","Has a technical degree; CS or equivalent","Experience in design, implementation and deployment experience of large-scale, distributed applications","Versed in experience architecting and implementing systems integration technologies","Ability to deliver high-quality, detailed-oriented documents Is adaptable to new (or old) technologies and learn quickly","Has a data-driven approach","Experience with a test-first approach","Willingness to be scrappy and experiment constantly to get to the key learnings and insights","Can prioritize based on impact and keep cross-functional teams focused Knowledge of modern web API technology"],
    'Data Scientist':["Strong programming skills, especially R and/or Python","Demonstrated experience in building, validating, and leveraging machine learning models","Demonstrated skill with data mining, data munging, coping with missing / corrupt / unstructured data","1+ years of industry experience building predictive models OR graduate-level research in a relevant area"]
}
brownie_points = {
    'Product Manager':["You have experience working with international teams across different locations"],
    'Frontend Engineer':["Experience delivering compelling experiences in SaaS or web-based solutions."],
    'Backend Engineer':["Relevant experience building large scale data systems."],
    'Software Engineer':["Relevant experience building large scale data systems."],
    'Fullstack Engineer':["have built microservices"],
    'Product Engineer':["Experience delivering compelling experiences in SaaS or web-based solutions."],
    'Head of Engineering':["Experience scaling platforms growing at pace."],
    'QA Engineer':["Understanding of the importance of test plans and how to approach writing informative bug reports"],
    'Android Engineer':[],
    'iOS Engineer':["Swift experience is a plus!"],
    'DevOps Engineer':[],
    'Data Scientist':["Experience using big data tools (e.g. Hadoop, Spark) and cloud computing (AWS preferred)","Advanced knowledge of physics, linear algebra, probability/statistics"]
}
feelfreetoapply="Feel free to apply even if you feel unsure about whether you meet every single requirement in this posting. As long as you're a quick learner, and are excited about changing the status quo for tech recruitment, we're happy to support you as you come up to speed with our tech stack."
perks = ["Flexible vacation","Catered lunch (5x per week)","$3k desk set up of your choice","Full medical, dental, and vision insurance","Paid parental leave","401K"]
tech_stack = ["ReactJS","NodeJS","Python","Django","AWS","MySQL"]
why_company = "We are still in the early stages of our journey. You will be working closely with our users, acting on both their feedback and what our data says. Things you build here will have tremendous impact on both our business and _*COMPANY*_ as a company."
after_application = ["Quick phone call with a member of our engineering team to find out more about your experience and why you want to work at _*COMPANY*_.","Onsite interview:",["Technical discussion with a senior engineer","Pairing on an interesting problem","Meet the founders"]]
eqaulity = "_*COMPANY*_ is an equal opportunity employer: we value diversity. We do not discriminate on the basis of race, religion, color, national origin, gender, sexual orientation, age, marital status, veteran status, or disability status."


role = st.sidebar.selectbox('Role',roles)
name = st.sidebar.text_input('Company Name',value="Google")
website = st.sidebar.text_input('Company Website',value="https://www.google.com")
url = st.sidebar.text_input('Logo URL',value="https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png")
location = st.sidebar.text_input('Job Location',value="World")

st.markdown('<img src="'+url+'" alt="URL incorrect">',unsafe_allow_html=True)
st.title(role+' at '+name)
st.markdown('<h4>Website: <a href="'+website+'">'+website+'</a></h4>',unsafe_allow_html=True)
st.markdown('<h4>Location: <b>'+location+'</b></h4>',unsafe_allow_html=True)

about_company = write_about_company(name)
for text in about_company:
    st.markdown('<p>'+text+'</p>',unsafe_allow_html=True)

st.markdown("<h2><b>What will I be doing?</b></h2>",unsafe_allow_html=True)
role_des = find_role_des(role,name)
st.markdown(role_des,unsafe_allow_html=True)

st.markdown("<h2><b>What do I need?</b></h2>",unsafe_allow_html=True)
role_req = find_role_req(role,name)
st.markdown(role_req,unsafe_allow_html=True)

st.markdown("<h2><b>Brownie Points</b></h2>",unsafe_allow_html=True)
bpoints = find_bpoints(role,name)
st.markdown(bpoints,unsafe_allow_html=True)

st.write(feelfreetoapply)

st.markdown("<h2><b>Perks</b></h2>",unsafe_allow_html=True)
perks = find_perks(role,name)
st.markdown(perks,unsafe_allow_html=True)

st.markdown("<h2><b>Tech Stack</b></h2>",unsafe_allow_html=True)
tstack = find_tstack(role,name)
l=len(tstack)
for i in range(l):
    st.markdown('<li>'+tstack[i]+'</li>',unsafe_allow_html=True)

st.markdown("<h2><b>Why "+name+"?</b></h2>",unsafe_allow_html=True)
st.write(why_company.replace('_*COMPANY*_',name))

st.markdown("<h2><b>What happens after I apply?</b></h2>",unsafe_allow_html=True)
afterapp = find_afterapp(role,name)
st.markdown(afterapp,unsafe_allow_html=True)

st.markdown("<h2><b>Equal employment opportunity</b></h2>",unsafe_allow_html=True)
st.write(eqaulity.replace('_*COMPANY*_',name))