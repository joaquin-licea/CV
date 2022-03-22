# Text Variables
Header = '> This resume was generated entirely in Python. For full sourcecode, view my github.'
Name = 'Joaquín Jesús Licea del Castillo'
Title = 'Economics'
Contact = 'Mexico City, Mx\n55-52-13-20-82\njoaquin.liceadelc@hotmail.com\nhttps://github.com/joaquin-licea'
ProfileHeader = 'PROFILE'
ProfileDesc = 'Hardworking recent graduate. Bringing forth a motivated attitude\nand a variety of powerful skills related to data analysis. Able to\ntranslate numbers into actionable strategies. Adept in general\naccounting and finance transactions. Committed to using my\nskills to add value for decision making.'
WorkHeader = 'EMPLOYMENT HISTORY'
WorkOneTitle = 'Budget Analyst, ISSFAM'
WorkOneTime = '08/2021-Present'
WorkOneDesc = '- Developed strategies to comply with budget goals.\n- Achieved budget goals and kept careful documentation of plans\n within structured databases.'
WorkTwoTitle = 'Financial Advisor, BPatrimonial'
WorkTwoTime = '10/2020-07/2021'
WorkTwoDesc = '- Aimed to meet the needs of long-term individual investors.\n- Managed all financial aspects of clients needs.'
WorkThreeTitle = 'Intern, Universidad Panamericana'
WorkThreeTime = '08/2019-07/2020'
WorkThreeDesc = '- Administrative tasks according to professor needs'
EduHeader = 'EDUCATION'
EduOneTitle = 'Economics, Universidad Panamericana (Titulation in process)'
EduOneTime = '2017-2021'
EduTwoTitle = 'Laws, Utel (Online)'
EduTwoTime = '2021-2024'
EduThreeTitle = 'International Political Economy Programme, London School\nof Economics and Political Science (London)'
EduThreeTime = 'June 2018'
EduFourTitle = 'The Challenges and New Threats to the Global Order,\nUniversidad Austral (Argentina)'
EduFourTime = 'June 2021'
EduFiveTitle = 'Investment Strategy Advisor (course), Peeptrade'
EduFiveTime = 'Sep 2021'
EduSixTitle = 'Programming for Financiers (course), Peeptrade'
EduSixTime = 'Jan 2022'
EduSevenTitle = 'TOEFL INSTITUCIONAL SCORE: 567'

SkillsHeader = 'Skills'
SkillsDesc = '- Python\n- Excel\n- NumPy\n- Visual Basic\n- Data Bases\n- Commercial Analysis\n- Team work\n- Fast learner\n- Data Analysis\n- Data Manipulation\n- Excel'
ExtrasTitle = 'Data Scientist Path'
ExtrasDesc = 'Learning popular data science\nlanguages, member of different\nNFT projects, machine learning\nand statistical analysis'

# Setting style for bar graphs
import matplotlib.pyplot as plt

# Set font
plt.rcParams['font.family'] = 'arial'
plt.rcParams['font.sans-serif'] = 'STIXGeneral'

fig, ax = plt.subplots(figsize=(8.5, 11))

# Decorative Lines
ax.axvline(x=.5, ymin=0, ymax=1, color='#007ACC', alpha=0.0, linewidth=50)
plt.axvline(x=.99, color='darkblue', alpha=0.5, linewidth=310)
plt.axhline(y=.88, xmin=0, xmax=1, color='#ffffff', linewidth=3)

# set background color
ax.set_facecolor('white')

# remove axes
plt.axis('off')

# add text
plt.annotate(Header, (.02,.98), weight='regular', fontsize=8, alpha=.6)
plt.annotate(Name, (.02,.94), weight='bold', fontsize=19)
plt.annotate(Title, (.02,.91), weight='regular', fontsize=13)
plt.annotate(Contact, (.7,.906), weight='bold', fontsize=9, color='#ffffff')
plt.annotate(ProfileHeader, (.02,.875), weight='bold', fontsize=10, color='darkblue')
plt.annotate(ProfileDesc, (.04,.79), weight='regular', fontsize=9)
plt.annotate(WorkHeader, (.02,.740), weight='bold', fontsize=10, color='darkblue')
plt.annotate(WorkOneTitle, (.02,.710), weight='bold', fontsize=10)
plt.annotate(WorkOneTime, (.02,.690), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkOneDesc, (.04,.640), weight='regular', fontsize=9)
plt.annotate(WorkTwoTitle, (.02,.610), weight='bold', fontsize=10)
plt.annotate(WorkTwoTime, (.02,.590), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkTwoDesc, (.04,.550), weight='regular', fontsize=9)
plt.annotate(WorkThreeTitle, (.02,.520), weight='bold', fontsize=10)
plt.annotate(WorkThreeTime, (.02,.500), weight='regular', fontsize=9, alpha=.6)
plt.annotate(WorkThreeDesc, (.04,.480), weight='regular', fontsize=9)
plt.annotate(EduHeader, (.02,.445), weight='bold', fontsize=10, color='darkblue')
plt.annotate(EduOneTitle, (.02,.420), weight='bold', fontsize=10)
plt.annotate(EduOneTime, (.02,.400), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduTwoTitle, (.02,.375), weight='bold', fontsize=10)
plt.annotate(EduTwoTime, (.02,.355), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduThreeTitle, (.02,.310), weight='bold', fontsize=10)
plt.annotate(EduThreeTime, (.02,.290), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduFourTitle, (.02,.245), weight='bold', fontsize=10)
plt.annotate(EduFourTime, (.02,.225), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduFiveTitle, (.02,.200), weight='bold', fontsize=10)
plt.annotate(EduFiveTime, (.02,.180), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduSixTitle, (.02,.150), weight='bold', fontsize=10)
plt.annotate(EduSixTime, (.02,.130), weight='regular', fontsize=9, alpha=.6)
plt.annotate(EduSevenTitle, (.02,.100), weight='bold', fontsize=10)

plt.annotate(SkillsHeader, (.7,.8), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(SkillsDesc, (.7,.56), weight='regular', fontsize=10, color='#ffffff')
plt.annotate(ExtrasTitle, (.69,.43), weight='bold', fontsize=10, color='#ffffff')
plt.annotate(ExtrasDesc, (.69,.345), weight='regular', fontsize=10, color='#ffffff')


plt.savefig('CV Joaquin Licea.pdf', dpi=300, bbox_inches='tight')