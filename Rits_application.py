import time
import socket
from urllib.request import *
import subprocess
import requests
import getpass
from bs4 import BeautifulSoup
import urllib.parse



username = None
password = None


def connect_network():

    if(check_dns_existence()):
        dns_servers_empty()


    if(check_network_connection()):
        print("Your computer can connect network :)")
        return True


    else:
        turn_on_wifi()

        time.sleep(1)

        if(check_network_connection()):
            print("Your computer can connect network :)")
            return True

        if(login_webauth()):
            if(check_network_connection()):
                print("Your computer can connect network :)")
                return True

            else:
                turn_off_wifi()

                turn_on_wifi

                turn_off_ipv6()

                if(check_network_connection()):
                    print("Your computer can connect network :)")
                    return True

                else:
                    print("I'm sorry. I can't connect wi-fi :(")
                    print("You may mistake 'User Name' or 'Password'")
                    print("Please try again!")
                    return False

        else:
            print("I'm sorry. I can't connect wi-fi :(")
            print("You may mistake 'User Name' or 'Password'")
            print("Please try again!")
            turn_off_wifi()
            return False

def input_form():

    global username
    global password

    if(username is None and password is None):

        # print("< Login Form >")

        # username = input("User Name :")
        # password = getpass.getpass("Password :")
        username = "xxx"
        password = "xxx"


def login_webauth():

    # <input type="hidden" name="buttonClicked" size="16" maxlength="15" value="0">
    # <input type="hidden" name="err_flag" size="16" maxlength="15" value="0">
    # <input type="hidden" name="err_msg" size="32" maxlength="31" value="">
    # <input type="hidden" name="info_flag" size="16" maxlength="15" value="0">
    # <input type="hidden" name="info_msg" size="32" maxlength="31" value="">
    # <input type="hidden" name="redirect_url" size="255" maxlength="255" value="">
    # <input type="hidden" name="network_name" size="64" maxlength="64" value="Guest Network">
    # <input type="TEXT" name="username" size="25" maxlength="80" value="">
    # <input type="Password" name="password" emweb_type="PASSWORD" autocomplete="off" onkeypress="submitOnEnter(event);" size="25" maxlength="127" value="">

    input_form()

    login_data = {

    "buttonClicked" : "4",
    "err_flag" : "0",
    "err_msg" : "",
    "info_flag" : "0",
    "info_msg" : "",
    "redirect_url" : "https://webauth.ritsumei.ac.jp/",
    "network_name" : "Guest Network",
    "username" : username,
    "password" : password

    }

    try:
        s = requests.Session()
        s.post("https://webauth.ritsumei.ac.jp/login.html",data=login_data)
        return True

    except:
        return False


def login_manaba():





    # <input class="input" id="User_ID" name="USER" type="text"/>
    # <input autocomplete="OFF" class="input" id="Password" name="PASSWORD" type="password"/></p>
    # <input class="submit" id="Submit" onclick="submitForm();" type="button" value="Sign On"/></p>
    # <input name="target" type="hidden" value="HTTPS://idp.ritsumei.ac.jp/pub/authtkt.cgi?back=http%3a%2f%2fidp.ritsumei.ac.jp%2fidp%2fAuthn%2fRemoteUser%3fconversation%3de1s1">
    # <input name="smauthreason" type="hidden" value="0">
    # <input name="smagentname" type="hidden" value="fkwCuvQ6h1Ls56sxQqE4EDvshnEHGeFZpJbGeHJa3fvdz0FkIbY+NOxc3BogXiIX"> random random
    # <input name="smquerydata" type="hidden" value="piA9EbF6/4pT06bKF++dfqm84azMaZ8qn9qnct2MZvV2VI5KIKqASXP0g3G0AqXWdgagatjLtrV7o7N3VExDK5kvcwWWzUXo30y7RcM/wbky2gQtgrF46g/3pHxtMp6kIma0tMTZjwOGVSIfkv3TxjNPmlUtSkyow1oELZhEZfSG2QMO0/LBzzhsS5RIAp4B7HwcG2TkOUKCJXrYIj/WrPPKcreo0AQf7boj8VqxXleYvcjlqij+7PCpePliZk7GLkpfU8q1UInJVQcYArReQ6kSBjkze1mEMEDBCy6rekl54jaeOSnR2SMKLnS5EkUXHKk1mXvUxEHiCxHqVJ9kftUo0RtWQ2wHimRqPQyxzl7CHp3qImGKMEf9xlXxjBmge0+BdKJFb5We0E3vWa7bEZwOWMT8azi2KpvUlhY4eBsdKU0bI4CoC9tJtJ2+J5x1aKJ+VlGLIjI3inX96jSikY5BOcKXxCYAKgmTpGQqKBpyYcjpxqlof8c14b/c7aEKbpnyV1DRmzILBIEWhXsOrnMHVvc7YcyH">
    # <input name="postpreservationdata" type="hidden" value="">



    login_data = {

    "USER" : username,
    "PASSWORD" : password,
    # "target" : "HTTPS://idp.ritsumei.ac.jp/pub/authtkt.cgi?back=http%3a%2f%2fidp.ritsumei.ac.jp%2fidp%2fAuthn%2fRemoteUser%3fconversation%3de1s1",
    "smauthreason" : "0",
    "smagentname" : "IT+z/ZUkK9dzQoHTzs1w047JL+8En4iEgfTWqOj+3bXo7P4+mbOpHc6lx+XSrc/b",
    # "smquerydata" : smquerydata_value,
    "postpreservationdata" : ""

    }



    request = requests.session()

    target_html = request.get("https://ct.ritsumei.ac.jp/ct/")

    target_html_text = BeautifulSoup(target_html.text.encode(target_html.encoding),"html.parser")

    target_value = target_html_text.find("input",{"name":"target"}).get("value")
    smquerydata_value = target_html_text.find("input",{"name":"smquerydata"}).get("value")

    login_data["target"] = target_value
    login_data["smquerydata"] = smquerydata_value


    smquerydata_value = smquerydata_value.replace("/","%2f")
    smquerydata_value = smquerydata_value.replace("+","%2b")

    target_url = "https://sso.ritsumei.ac.jp/siteminderagent/forms/login.fcc?SMQUERYDATA=-SM-" + smquerydata_value
    # print(target_url)



    # print(username + "\n")
    # print(password + "\n")
    # print(target_value + "\n")
    # print(smagentname_value + "\n")
    # print(smquerydata_value + "\n")
    #
    # print(login_data)
    # print(target_url)

    #make cookie

    run_javascript(target_url)
    escaped = open("escaped","r")

    cookies = {

    "path" : "/",
    "domain" : "ritsumei.ac.jp",
    "backurl" : escaped.read(),
    "ELM_UserID" : username,
    "ELM_PwPhrase" : password,
    "usr" : username,
    "rpwd" : password,

    }


    try:
        print(login_data)
        print(cookies)
        a = request.get(target_url + "/cgi-bin/pwexpcheck.cgi/",cookies=cookies)
        print(a.cookies)
        b = request.post(target_url + "/cgi-bin/pwexpcheck.cgi/",data=login_data)
        print(b.cookies)


        return True

    except Exception as error:
        print(error)
        return False





def get_ip_address():

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        s.connect(("8.8.8.8",100))
        ip_address = s.getsockname()[0]
        return True

    except:
        return False




def check_network_connection():

    try:
        urlopen("https://www.google.co.jp/")
        return True

    except:
        return False

def run_javascript(url):

    try:
        command= "sudo node escape.js " + url
        result = subprocess.check_output(command.split(" "))
        return True

    except Exception as error:
        print(error)
        return False


def dns_servers_empty():
    command= "sudo networksetup -setdnsservers Wi-Fi Empty"
    result = subprocess.check_output(command.split(" "))

    return str(result)

def check_dns_existence():
    command= "sudo networksetup -getdnsservers Wi-Fi"
    result = subprocess.check_output(command.split(" "))


    if("DNS" in str(result)):
        return False

    else:
        return True

def turn_off_ipv6():
    command= "sudo networksetup -setv6off Wi-Fi"
    result = subprocess.check_output(command.split(" "))

    return True

def turn_on_wifi():
    command= "sudo networksetup -setairportpower Wi-Fi on"
    result = subprocess.check_output(command.split(" "))

    return True

def turn_off_wifi():
    command= "sudo networksetup -setairportpower Wi-Fi off"
    result = subprocess.check_output(command.split(" "))

    return True

def res_cmd(cmd):
  return subprocess.Popen(
      cmd, stdout=subprocess.PIPE,
      shell=True).communicate()[0]


if __name__ == '__main__':


    time.sleep(5)
    res_cmd('networksetup -setairportpower en0 on')
    time.sleep(5)
    res_cmd('networksetup -setairportnetwork en0 Rits-Webauth webauth.ritsumei.ac.jp')
    login_webauth()
    # login_manaba()

    # if(connect_network()):
    #     print("See you latar!!")
    #
    # else:
    #     if(connect_network()):
    #         print("See you later!!")
    #
    #     else:
    #         print("I can't do anything... Sorry:(")
