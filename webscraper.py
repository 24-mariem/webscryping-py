from selenium import webdriver

url = 'https://www.youtube.com/channel/UC0LF4xChxmRruoyKMB5dAzw/videos'
browser = webdriver.Chrome('/Users/waldon/Documents/python/webScraping/chromedriver')
browser.implicitly_wait(10)
browser.get(url)
browser.find_element_by_xpath('//*[@id="yDmH0d"]/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/form[2]').click()
browser.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]/div[1]/ytd-thumbnail/a').click()
