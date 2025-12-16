                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-Mode': 'navigate',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'Host': 'www.instagram.com',
                                Println(Panel(f"[bold white]Berhasil menghapus semua tautan yang terhubung dalam akun like4like kamu, sekarang kamu dapat menukarkan koin ke pengikut instagram!", width=59, style="bold bright_black", title="[bold bright_black]>> [Sukses] <<"))
                exit()
            elif self.choices in ['4', '04']:
                Println(Panel(f"[bold white]Berhasil menghapus cookies instagram dan like4like, terimakasih telah menggunakan layanan kami!", width=59, style="bold bright_black", title="[bold bright_black]>> [Keluar] <<"))
                os.remove('Penyimpanan/Cookies.json')
                exit()
            else:
                Println(Panel(f"[bold red]Pilihan yang kamu masukan tidak ada dalam fitur kami, silahkan masukan pilihan dengan benar!", width=59, style="bold bright_black", title="[bold bright_black]>> [Pilihan Salah] <<"))
                time.sleep(4.5)
                Fitur()
        except Exception as e:
            Println(Panel(f"[bold red]{str(e).capitalize()}!", width=59, style="bold bright_black", title="[bold bright_black]>> [Error] <<"))
            exit()

class Menghapus:

    def __init__(self) -> None:
        pass

    def Link(self, cookies: str) -> bool:
        while True:
            with requests.Session() as r:
                r.headers.update({
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                    'Sec-Fetch-Site': 'same-origin',
                    'Sec-Fetch-Mode': 'navigate',
                    'Connection': 'keep-alive',
                    'Host': 'www.like4like.org',
                    'Upgrade-Insecure-Requests': '1',
                    'Sec-Fetch-Dest': 'document',
                    'User-Agent': 'Mozilla/5.0 (Linux; Android 13; Pixel 6 Pro) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36',
                    'Sec-Fetch-User': '?1',
                    'Accept-Language': 'en-US,en;q=0.9',

                })
                response = r.get('https://www.like4like.org/user/manage-my-pages.php', cookies = {
                    "Cookie": cookies
                })
                try:
                    self.featureName = re.search(r'window.location = ".*?=(.*?)"', str(response.text)).group(1)
                    self.idzadatka = re.search(r'"add-.*?-credits-id(\d+)"', str(response.text)).group(1)
                except AttributeError:
                    Println(f"[bold bright_black]   ╰─>[bold red] TIDAK MENEMUKAN USER YANG TERKAIT!     ", end='\r')
                    time.sleep(2.5)
                    break
                r.headers.pop("Upgrade-Insecure-Requests")
                r.headers.update({
                    'Referer': 'https://www.like4like.org/user/manage-my-pages.php',
                    'X-Requested-With': 'XMLHttpRequest',
                    'Sec-Fetch-Mode': 'cors',
                    'Accept': 'application/json, text/javascript, */*; q=0.01',
                    'Origin': 'https://www.like4like.org',
                    'Sec-Fetch-Dest': 'empty',
                    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                })
                data = {
                    'featureName': self.featureName,
                    'idzadatka': self.idzadatka,
                }
                response2 = r.post('https://www.like4like.org/api/archive-task.php', data = data, cookies = {
                    "Cookie": cookies
                })
                if '"success":true' in str(response2.text) and '"errors":[]' in str(response2.text):
                    response3 = r.post('https://www.like4like.org/api/delete-task.php', data = data, cookies = {
                        "Cookie": cookies
                    })
                    if '"success":true' in str(response3.text) and '"error":null' in str(response3.text):
                        Println(f"[bold bright_black]   ╰─>[bold green] SUKSES MENGHAPUS @{self.idzadatka}!     ", end='\r')
                        time.sleep(2.5)
                        continue
                    else:
                        Println(f"[bold bright_black]   ╰─>[bold green] SUKSES MENGARSIPKAN @{self.idzadatka}!    ", end='\r')
                        time.sleep(2.5)
                        continue
                else:
                    Println(f"[bold bright_black]   ╰─>[bold red] GAGAL MENGHAPUS @{self.idzadatka}!     ", end='\r')
                    time.sleep(2.5)
                    return False
        return True

class Mission:

    def __init__(self) -> None:
        pass

    def Delay(self, menit: int, detik: int) -> None:
        self.total = (menit * 60 + detik)
        while (self.total):
            menit, detik = divmod(self.total, 60)
            Println(f"[bold bright_black]   ╰─>[bold white] TUNGGU[bold green] {menit:02d}:{detik:02d}[bold white] SUKSES:-[bold green]{len(SUKSES)}[bold white] GAGAL:-[bold red]{len(GAGAL)}     ", end='\r')
            time.sleep(1)
            self.total -= 1
        return None

    def Like4Like(self, cookies_like4like: str, cookies_instagram: str, delay: int) -> bool:
        with requests.Session() as session:
            Bypass().Spam(session, cookies_like4like)
            session.headers.update({
                'Referer': 'https://www.like4like.org/user/earn-instagram-follow.php',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Sec-Fetch-Mode': 'cors',
                'Sec-Fetch-Dest': 'empty',
                'X-Requested-With': 'XMLHttpRequest',
            })
            response = session.get('https://www.like4like.org/api/get-tasks.php?feature=instagramfol', cookies = {
                "Cookie": cookies_like4like
            })
            if '"success":true,' in str(response.text) and 'www.instagram.com' in str(response.text):
                for z in json.loads(response.text)['data']['tasks']:
                    self.timestamp_milliseconds = str(datetime.datetime.now().timestamp() * 1000).split('.')[0]
                    self.idlink, self.taskId, self.code3 = z['idlink'], z['taskId'], z['code3']
                    session.headers.update({
                        'Content-Type': 'application/json; charset=utf-8',
                    })
                    response2 = session.get(f'https://www.like4like.org/api/start-task.php?idzad={self.idlink}&vrsta=follow&idcod={self.taskId}&feature=instagramfol&_={self.timestamp_milliseconds}', cookies = {
                        "Cookie": cookies_like4like
                    })
                    if '"success":true,' in str(response2.text):
                        session.headers.update({
                            'Content-Type': 'application/x-www-form-urlencoded',
                            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                            'Sec-Fetch-Mode': 'navigate',
                            'Sec-Fetch-Dest': 'document',
                            'Origin': 'https://www.like4like.org',
                        })
                        data = {
                            'url': f'https://www.instagram.com/{self.idlink}',
                        }
                        response3 = session.post('https://www.like4like.org/checkurl.php', data = data, cookies = {
                            'Cookie': cookies_like4like
                        })
                        if 'https://www.instagram.com/' in str(response3.text) or 'https://freesocialmediatrends.com/l/loadurl.php' in str(response3.text):
                            self.Mengikuti(cookies_instagram, session, username = self.idlink)
                            time.sleep(5.0)
                            session.headers.update({
                                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                                'Accept': 'application/json, text/javascript, */*; q=0.01',
                                'Origin': 'https://www.like4like.org',
                                'Accept-Language': 'en-US,en;q=0.9',
                                'Sec-Fetch-Dest': 'empty',
                                'Sec-Fetch-Site': 'same-origin',
                                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                                'Host': 'www.like4like.org',
                                'Sec-Fetch-Mode': 'cors',
                                'Referer': 'https://www.like4like.org/user/earn-instagram-follow.php',
                            })
                            data = {
                                'url': f'https://www.instagram.com/{self.idlink}',
                                'idlinka': f'{self.idlink}',
                                'idzad': f'{self.taskId}',
                                'addon': False,
                                'version': '',
                                'idclana': f'{self.code3}',
                                'cnt': True,
                                'vrsta': 'follow',
                                'feature': 'instagramfol',
                            }
                            response4 = session.post('https://www.like4like.org/api/validate-task.php', data = data, cookies = {
                                'Cookie': cookies_like4like
                            })
                            if '"success":true,' in str(response4.text) and '"credits"' in str(response4.text):
                                self.penambahan_credits = re.search(r'"credits":"(.*?)"', str(response4.text)).group(1)
                                Println(Panel(f"""[bold white]Status :[bold green] Successfully...
[bold white]Link :[bold red] https://www.instagram.com/{self.idlink}
[bold white]Credits :[bold green] {CREDITS['COUNT']}[bold white] >[bold green] {self.penambahan_credits}""", width=59, style="bold bright_black", title="[bold bright_black]>> [Sukses] <<"))
                                SUKSES.append(f'{str(response4.text)}')
                                CREDITS.update({
                                    "COUNT": int(self.penambahan_credits)
                                })
                                return True
                            else:
                                Println(f"[bold bright_black]   ╰─>[bold red] @{self.idlink} GAGAL MENDAPATKAN KOIN!     ", end='\r')
                                time.sleep(3.5)
                                return False
                        else:
                            Println(f"[bold bright_black]   ╰─>[bold red] TIDAK MENDAPATKAN REDICT URL!         ", end='\r')
                            time.sleep(4.0)
                            return False
                    else:
                        Println(f"[bold bright_black]   ╰─>[bold red] TIDAK MENDAPATKAN TASK KODE!          ", end='\r')
                        time.sleep(4.0)
                        return False
            elif 'tasks' not in str(response.text):
                Println(f"[bold bright_black]   ╰─>[bold red] ANDA TERDETEKSI SEBAGAI BOT!    ", end='\r')
                time.sleep(10.0)
                return False
            else:
                Println(f"[bold bright_black]   ╰─>[bold red] SEDANG TIDAK ADA MISI!          ", end='\r')
                time.sleep(5.0)
                return False
            
    def Mengikuti(self, cookies_instagram: str, session: requests.Session, username: str) -> bool:
        session.headers.clear()
        session.headers.update({
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'navigate',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Host': 'www.instagram.com',
            'Sec-Fetch-Dest': 'document',
            'Accept-Language': 'en-US,en;q=0.9',
        })
        response = session.get('https://www.instagram.com/{}'.format(username).replace('@', ''), cookies = {
            'Cookie': cookies_instagram
        })
        self.profilePage = re.search(r'"profilePage_(\d+)"', str(response.text)).group(1)
        session.headers.update({
            'Referer': 'https://www.instagram.com/{}'.format(username),
            'X-IG-App-ID': '936619743392459',
            'X-Requested-With': 'XMLHttpRequest',
            'Sec-Fetch-Mode': 'cors',
            'X-Instagram-AJAX': '1012867433',
            'X-IG-WWW-Claim': '0',
            'X-CSRFToken': re.search(r'csrftoken=(.*?);', str(cookies_instagram)).group(1),
            'Accept': '*/*',
            'X-ASBD-ID': '129477',
            'Sec-Fetch-Dest': 'empty',
            'Origin': 'https://www.instagram.com',
            'Content-Type': 'application/x-www-form-urlencoded',
        })
        data = {
            'container_module': 'profile',
            'nav_chain': 'PolarisProfilePostsTabRoot:profilePage:1:via_cold_start',
            'user_id': self.profilePage,
        }
        response2 = session.post('https://www.instagram.com/api/v1/friendships/create/{}/'.format(self.profilePage), data = data, cookies = {
            'Cookie': cookies_instagram
        })
        session.headers.clear()
        if '"following":true,' in str(response.text):
            return True
        else:
            return False

class Tukarkan:

    def __init__(self) -> None:
        pass

    def Pengikut(self, cookies: str, credits_: str, fblink: str, fbcredits: str) -> None:
        with requests.Session() as session:
            session.headers.update({
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Sec-Fetch-Site': 'same-origin',
                'Sec-Fetch-Mode': 'navigate',
                'Connection': 'keep-alive',
                'Host': 'www.like4like.org',
                'Sec-Fetch-Dest': 'document',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
                'Sec-Fetch-User': '?1',
                'Accept-Language': 'en-US,en;q=0.9',
            })
            response = session.get('https://www.like4like.org/user/manage-my-pages.php?feature=instagramfol', cookies = {
                "Cookie": cookies
            })
            session.headers.update({
                'Referer': 'https://www.like4like.org/user/manage-my-pages.php?feature=instagramfol',
                'X-Requested-With': 'XMLHttpRequest',
                'Sec-Fetch-Mode': 'cors',
                'Accept': 'application/json, text/javascript, */*; q=0.01',
                'Origin': 'https://www.like4like.org',
                'Sec-Fetch-Dest': 'empty',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            })
            data = {
                'idclana': '3740207',
                'fbdescription': '',
                'feature': 'instagramfol',
                'fblink': fblink,
                'fbcredits': fbcredits,
            }
            self.jumlah = (int(credits_) / int(fbcredits))
            response2 = session.post('https://www.like4like.org/api/enterlink.php', data = data, cookies = {
                "Cookie": cookies
            })
            if '"uradio"' in str(response2.text):
                Println(Panel(f"""[bold white]Status :[bold green] Currently processing your order...
[bold white]Link :[bold red] {fblink}
[bold white]Followers :[bold green] {int(self.jumlah)}""", width=59, style="bold bright_black", title="[bold bright_black]>> [Sukses] <<"))
                return None
            else:
                Println(Panel(f"[bold red]Maaf, kami tidak bisa menukarkan koin anda ke pengikut, anda bisa mencoba menukarkan secara manual!", width=59, style="bold bright_black", title="[bold bright_black]>> [Gagal] <<"))
                exit()

if __name__ == '__main__':
    try:
        if os.path.exists("Penyimpanan/Subscribe.json") == False:
            youtube_url = json.loads(requests.get('https://raw.githubusercontent.com/RozhakXD/Like4Gram/main/Penyimpanan/Youtube.json').text)['Link']
            os.system(f'xdg-open {youtube_url}')
            with open('Penyimpanan/Subscribe.json', 'w') as w:
                w.write(json.dumps({
                    "Status": True
                }))
            w.close()
            time.sleep(2.5)
        os.system('git pull')
        Fitur()
    except Exception as e:
        Println(Panel(f"[bold red]{str(e).capitalize()}!", width=59, style="bold bright_black", title="[bold bright_black]>> [Error] <<"))
        exit()
    except KeyboardInterrupt:

        exit()
