from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

import time

def upload_clips(clips, title, description):
    vid_num = 2
    options = Options()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument("--disable-extensions")

    options.add_experimental_option("prefs", { 
        "profile.default_content_setting_values.notifications": 2 
    })
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options, executable_path="driver/chromedriver.exe")
    driver.get('<link to youtube channel>')

    #goes through upload process
    sign_in_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='buttons']/ytd-button-renderer/a")))
    sign_in_button.click()

    login_email = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierId']")))
    login_email.send_keys('<email to youtube account>')

    email_next_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='identifierNext']/div/button")))
    email_next_button.click()

    login_password = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='password']/div[1]/div/div[1]/input")))
    login_password.send_keys('<password to youtube account>')

    password_next_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='passwordNext']/div/button")))
    password_next_button.click()

    create_videos_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[3]/div[2]/ytd-topbar-menu-button-renderer[1]/div/a/yt-icon-button/button/yt-icon")))
    create_videos_button.click()

    upload_videos_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytd-app/ytd-popup-container/tp-yt-iron-dropdown/div/ytd-multi-page-menu-renderer/div[3]/div[1]/yt-multi-page-menu-section-renderer/div[2]/ytd-compact-link-renderer[1]/a/tp-yt-paper-item")))
    upload_videos_button.click()

    select_files_button = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-uploads-file-picker/div/input")))
    select_files_button.send_keys('D:/zgarw/Documents/Projects/autoclip/fin/' + title + '.mp4')

    title_with_vid = clips[vid_num]['title'].upper() + ' - ' + title
    while(len(title_with_vid) > 100):
        vid_num += 1
        title_with_vid = clips[vid_num]['title'].upper() + ' - ' + title

    title_area = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[1]/ytcp-mention-textbox/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div")))
    title_area.clear();
    title_area.send_keys(title_with_vid)

    description_area = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[2]/ytcp-mention-textbox/ytcp-form-input-container/div[1]/div[2]/ytcp-mention-input/div")))
    description_area.send_keys(description)

    upload_thumbnail = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[3]/ytcp-thumbnails-compact-editor/div[3]/ytcp-thumbnails-compact-editor-uploader/input")))
    upload_thumbnail.send_keys('D:/zgarw/Documents/Projects/autoclip/img/' +clips[vid_num]['slug'] + '.jpg')

    upload_videos_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/div/ytcp-button")))
    upload_videos_button.click()

    made_for_kids = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-basics/div[5]/ytkc-made-for-kids-select/div[4]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[2]")))
    made_for_kids.click()

    tags_area = WebDriverWait(driver, 1000).until(EC.presence_of_element_located((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-video-metadata-editor/div/ytcp-video-metadata-editor-advanced/div[3]/ytcp-form-input-container/div[1]/div[2]/ytcp-free-text-chip-bar/ytcp-chip-bar/div/input")))
    tags_area.send_keys('Twitch Clips, Top Clips, Daily, Top Clips of the Day, Streaming')

    details_next_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]")))
    details_next_button.click()

    video_elements_next_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]")))
    video_elements_next_button.click()

    checks_next_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[2]/div/div[2]/ytcp-button[2]")))
    checks_next_button.click()

    visibility_public_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-dialog/tp-yt-paper-dialog/div/ytcp-animatable[1]/ytcp-uploads-review/div[2]/div[1]/ytcp-video-visibility-select/div[1]/tp-yt-paper-radio-group/tp-yt-paper-radio-button[3]")))
    visibility_public_button.click()

    publish_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#done-button[aria-disabled='false']")))
    publish_button.click()

    close_button = WebDriverWait(driver, 1000).until(EC.element_to_be_clickable((By.XPATH, "/html/body/ytcp-uploads-still-processing-dialog/ytcp-dialog/tp-yt-paper-dialog/div[3]/ytcp-button")))
    close_button.click()


    
    