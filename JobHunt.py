from bs4 import BeautifulSoup
import  requests
import time as t

print('Enter a skill to filter out that you  don\'t want to see')
fliterSkills = input('> ')
def ScapperApp():
    link = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text

    soup = BeautifulSoup(link,'lxml')

    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    print('please wait fatching ....')
    job_number =0
    for  job in jobs:
                job_number+=1
                company_name = job.find('h3', class_='joblist-comp-name').text.strip()
                Job_level = job.find('ul',class_='top-jd-dtl clearfix').li.text.strip().replace('card_travel','')
                Description = job.find('ul', class_='list-job-dtl clearfix').li.text.strip().replace('Job Description:','')
                skills = job.find('span',class_='srp-skills').text.strip().replace(' ','')
                # apply = soup.find('header', class_='clearfix')
                post_time = job.find('span',class_='sim-posted').span.text.strip()
                more_info = job.header.h2.a['href']

                if  fliterSkills not in skills:
                    with open (f'Jobs/{company_name}.txt','w') as f:
                        f.write(f'{job_number}. Company Name : {company_name}\n')
                        f.write(f'Job exprinece required: {Job_level}\n')
                        f.write(f'Skills: {skills}\n')
                        f.write('')
                        f.write(f'Description : {Description}\n')
                        f.write(f'More info: {str(more_info)}\n')
                        f.write(f'posted time : {post_time}\n ')
                        f.write('')
                        # print('=======================================================================================================================================')
                    print(f'File saved  as {company_name}.txt')

if __name__=='__main__':
    # while True:
    #     wait = 10
    #     ScapperApp()
    #     print('\n\n\n')
    #     print(f'Waiting for {wait} mins')
    #     print('\n\n\n')
    #     t.sleep(10)
    ScapperApp()