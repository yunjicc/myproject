import pyautogui
import pyperclip
import time
import math

# --- 📍 추출한 좌표를 여기에 입력하세요 ---
CHROME_ICON = (44, 299)             # 크롬 아이콘 위치
ACCOUNT_BUTTON = (1076, 598)        # 계정(Jihoo Yu) 위치
BOOKMARK_BAR = (181, 128)           # 북마크 보고서 위치
BST_BUTTON = (191, 414)             # Brand Search Trends 버튼 위치
DATE_BUTTON = (1799, 321)           # 날짜 버튼 위치
S_YEAR_BUTTON = (1419, 478)         # 시작년도 버튼 위치
Y2024_BUTTON = (1346, 613)          # 2024년 선택
Y2024_1_BUTTON = (1339, 580)        # 2024년 1월 선택
Y2024_1_1_BUTTON = (1360, 606)      # 2024년 1월 1일 선택
E_YEAR_BUTTON = (1700, 487)         # 종료년도 버튼 위치
Y2025_BUTTON = (1666, 608)          # 2025년 선택
Y2025_12_BUTTON = (1789, 646)       # 2025년 12월 선택
Y2025_12_31_BUTTON = (1702, 739)    # 2024년 12월 31일 선택
SELECT_DATE_BUTTON = (1800, 771)    # 날짜 필터 적용

filter_coords = {
    "COUNTRY": {
        "BUTTON": (670, 322),         # 국가 필터 클릭
        "SEARCH_BUTTON": (676, 376),  # 국가 검색
        "SELECT_BUTTON": (830, 423),  # 국가 선택
        "CLOSE_BUTTON": (687, 251)    # 국가 필터 종료
    },

    "BRAND": {
        "BUTTON": (824, 320),              # 브랜드 필터 클릭
        "SEARCH_BUTTON": (826, 373),       # 브랜드 검색
        "SELECT_BUTTON": (1013, 422),      # 브랜드 선택
        "CLOSE_BUTTON": (903, 250)         # 브랜드 필터 종료
    },

    "PL": {
        "BUTTON": (1026, 321),              # pl 필터 클릭
        "SEARCH_BUTTON": (1044, 376),       # pl 검색
        "SELECT_BUTTON": (1193, 428),       # pl 선택
        "CLOSE_BUTTON": (1087, 251)         # pl 필터 종료
    },

    "MODEL": {
        "BUTTON": (1182, 320),              # model 필터 클릭
        "UNFILTER_BUTTON": (1122, 327),     # 첫 시작 전, 필터 전체 해제
        "SEARCH_BUTTON": (1185, 377),       # model 검색
        "SELECT_BUTTON": (1124, 424),       # model 선택
        "SELECT_ONLY": (1361, 426),       # model 지정한 값만 선택
        "CLOSE_BUTTON": (1087, 251)         # model 필터 종료
    }
}

SCROLL_BAR = (1917, 319)            # 상단, 스크롤바 
FILE_NAME_CLICK = (956, 400)        # 파일 이름 변경 (후에 전체지우기_)
EXTRACT_BUTTON = (1145, 813)        # 파일 내보내기
# ---------------------------------------

def start_full_automation():
    try:
        print("🚀 자동화를 시작합니다. 마우스에서 손을 떼세요!")

        # 1. 바탕화면 크롬 더블클릭
        pyautogui.doubleClick(CHROME_ICON)
        print("1. 크롬 실행 중...")
        time.sleep(1) # 브라우저 켜지는 시간 대기

        # 2. 창 최대화 (단축키 Win + Up)
        pyautogui.hotkey('win', 'up')

        # 3. 계정 선택 클릭
        print("2. 계정 선택 중...")
        pyautogui.click(ACCOUNT_BUTTON)
        time.sleep(2) # 로그인 후 페이지 전환 대기

        # 4. 북마크 클릭 (루커스튜디오 이동)
        print("3. 북마크 클릭 중...")
        pyautogui.click(BOOKMARK_BAR)
        
        # 5. 루커스튜디오 로딩
        print("4. 보고서 로딩 대기 중 (7초)...")
        time.sleep(7)

        # 6. BST 탭 선택
        print("5. BST 탭 선택 중 7초)...")
        pyautogui.click(BST_BUTTON)
        time.sleep(7)

        # 7. 날짜 선택 (2024-01-01 ~ 2025-12-31)
        print("5. 날짜 선택 중 10초)...")
        pyautogui.click(DATE_BUTTON)
        pyautogui.click(S_YEAR_BUTTON)
        pyautogui.click(Y2024_BUTTON)
        pyautogui.click(Y2024_1_BUTTON)
        pyautogui.click(Y2024_1_1_BUTTON)
        pyautogui.click(E_YEAR_BUTTON)
        pyautogui.click(Y2025_BUTTON)
        pyautogui.click(Y2025_12_BUTTON)
        pyautogui.click(Y2025_12_31_BUTTON)
        pyautogui.click(SELECT_DATE_BUTTON)
        time.sleep(7)
        
        print("✅ 모든 동작이 완료되었습니다!")

    except Exception as e:
        print(f"❌ 에러 발생: {e}")

def filter(filter_type, value):
    # filter_type이 "COUNTRY"면 COUNTRY 좌표를, "BRAND"면 BRAND 좌표를 가져옴
    coords = filter_coords[filter_type]

    try:
        print(f"🌍 {filter_type} Filter Setting for: {value}")

        # 1. 필터 버튼 클릭1
        pyautogui.click(coords["BUTTON"])

        # 2. 검색창 클릭 및 기존 내용 삭제
        # 3. 국가/브랜드명 타이핑 (interval을 주면 더 안정적입니다)
        pyautogui.click(coords["SEARCH_BUTTON"])
        pyperclip.copy(value)
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)

        # 4. 첫 번째 검색 결과 클릭
        pyautogui.click(coords["SELECT_BUTTON"], clicks=2, interval=0.1)
        time.sleep(0.5)

        # 5. 필터 창 닫기 (Esc)
        pyautogui.click(coords["CLOSE_BUTTON"])
        print(f"✅ {value} applied.")
        
        # 6. 데이터 업데이트 대기 (보고서 사양에 따라 조절)
        time.sleep(2)
        
    except Exception as e:
        print(f"❌ 에러 발생: {e}")  


def filter_model(chunk):
    coords = filter_coords["MODEL"]

    # 1. 필터 버튼 클릭-> 전체 해제
    pyautogui.click(coords["BUTTON"])

    # 2. 검색창 클릭 및 기존 내용 삭제
    for i in range(len(chunk)):
        pyautogui.click(coords["SEARCH_BUTTON"])
        pyperclip.copy(chunk[i])
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.2)
        if i == 0:
            pyautogui.click(coords["SELECT_ONLY"])
            time.sleep(0.2)
        else:
            pyautogui.click(coords["SELECT_BUTTON"])
            # time.sleep(0.1)   

    # 5. 필터 창 닫기 (Esc)
    pyautogui.click(coords["CLOSE_BUTTON"])
    print("✅applied.")
        
    # 6. 데이터 업데이트 대기 (보고서 사양에 따라 조절)
    time.sleep(2)   

def get_chunks(lst, n):
    """리스트 lst를 n개씩 조각내어 반환하는 함수"""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]

def unfilter():
    try:
        coords = filter_coords["PL"]
        pyautogui.click(973, 313)
        pyautogui.click(932, 324)
        pyautogui.click(869, 259)
        time.sleep(0.7)
            
    except Exception as e:
        print(f"❌ 에러 발생: {e}")  

def by_brand(country):
    try:
        print(f"-- Scroll Down for by_Brand --")
        pyautogui.moveTo(SCROLL_BAR)
        pyautogui.scroll(-500) # 음수(-)는 아래로, 양수(+)는 위로 스크롤
        
        ## MONTHLY
        pyautogui.moveTo(x=1626, y=513) # 데이터 추출 점 3개 띄우기
        time.sleep(3)
        pyautogui.click(x=1555, y=412)  #Monthly 선택
        time.sleep(3)
        pyautogui.click(x=1713, y=397)  #더보기 선택
        time.sleep(3)
        pyautogui.click(x=1592, y=578) #차트 내보내기 클릭
        time.sleep(3)
        pyautogui.click(x=1422, y=585) #데이터 내보내기 클릭
        pyautogui.click(FILE_NAME_CLICK)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.press('backspace') 
        time.sleep(1)
        pyautogui.write(country+"_Monthly_by Brand", interval=0.05)
        pyautogui.click(EXTRACT_BUTTON)
        time.sleep(3)

        ## DAILY
        pyautogui.click(1699, 823)
        time.sleep(3)
        pyautogui.click(1137, 542)
        time.sleep(3)
        pyautogui.click(x=1587, y=404)  #Daily 선택
        time.sleep(3)
        pyautogui.click(x=1713, y=397)  #더보기 선택
        time.sleep(3)
        pyautogui.click(x=1592, y=578) #차트 내보내기 클릭
        time.sleep(3)
        pyautogui.click(x=1422, y=585) #데이터 내보내기 클릭
        pyautogui.click(FILE_NAME_CLICK)
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.press('backspace') 
        time.sleep(1)
        pyautogui.write(country+"_Daily_by Brand", interval=0.05)
        pyautogui.click(EXTRACT_BUTTON)

        pyautogui.moveTo(1913, 450)
        pyautogui.scroll(+500)
        pyautogui.moveTo(SCROLL_BAR)
        pyautogui.scroll(+500)
        time.sleep(1.5)

    except Exception as e:
        print(f"❌ 에러 발생: {e}")  

def by_pl(country, brand):
    try:
        print(f"-- Scroll Down for by_Product Lines --")
        pyautogui.moveTo(SCROLL_BAR)
        pyautogui.scroll(-500)
        pyautogui.moveTo(1913, 450)
        pyautogui.scroll(-600)

        time.sleep(1.5)
        ## MONTHLY
        print(f"-- MONTHLY --")
        pyautogui.moveTo(1675, 547) # 데이터 추출 점 3개 띄우기
        time.sleep(1)
        pyautogui.click(1520, 380)  #Monthly 선택
        time.sleep(3)
        pyautogui.click(1675, 382)  #더보기 선택
        time.sleep(0.3)
        pyautogui.click(1737, 559) #차트 내보내기 클릭
        time.sleep(0.2)
        pyautogui.click(1600, 565) #데이터 내보내기 클릭
        pyautogui.click(FILE_NAME_CLICK)
        pyperclip.copy(f"{country}_Monthly_by Product Line_{brand}")
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(x=1173, y=850) #EXTRACT
        time.sleep(2)

        ## DAILY
        print(f"-- DAILY --")        
        pyautogui.click(x=1648, y=835)
        time.sleep(1)
        pyautogui.click(1564, 387)  #Daily 선택
        time.sleep(1)
        pyautogui.click(1675, 382)  #더보기 선택
        time.sleep(0.3)
        pyautogui.click(1737, 559) #차트 내보내기 클릭
        time.sleep(0.2)
        pyautogui.click(1600, 565) #데이터 내보내기 클릭
        pyautogui.click(FILE_NAME_CLICK)
        pyperclip.copy(f"{country}_Daily_by Product Line_{brand}")
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(x=1173, y=850) #EXTRACT

        pyautogui.moveTo(1913, 450)
        pyautogui.scroll(+500)
        pyautogui.moveTo(SCROLL_BAR)
        pyautogui.scroll(+600)
        time.sleep(1.5)

    except Exception as e:
        print(f"❌ 에러 발생: {e}")  
 
def by_model(country, brand, pl, i=None):
    try:
        print(f"-- Scroll Down for by_Product Lines --")
        pyautogui.moveTo(SCROLL_BAR)
        pyautogui.scroll(-500)
        pyautogui.moveTo(1913, 450)
        pyautogui.scroll(-500)
        pyautogui.moveTo(1914, 550)
        pyautogui.scroll(-700)

        time.sleep(2)
        ## MONTHLY
        print(f"-- MONTHLY --")
        pyautogui.moveTo(1591, 834) # 데이터 추출 점 3개 띄우기
        time.sleep(1)
        pyautogui.click(1529, 370)  #Monthly 선택
        time.sleep(4)
        pyautogui.click(1679, 370) #더보기 선택
        time.sleep(0.2)
        pyautogui.click(1727, 555) #차트 내보내기 클릭
        time.sleep(0.1)
        pyautogui.click(1565, 555) #데이터 내보내기 클릭
        pyautogui.click(1001, 384) #file name
        pyperclip.copy(f"{country}_Monthly_by Model_{brand}_{pl}_{i}")
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(1160, 839) #extract
        pyautogui.click(1773, 833)
        time.sleep(2)

        ## DAILY
        print(f"-- DAILY --")
        pyautogui.doubleClick(x=1391, y=887)
        time.sleep(2)
        pyautogui.click(1567, 370)  #Daily 선택
        time.sleep(3)
        pyautogui.click(1682, 370) #더보기 선택
        time.sleep(0.2)
        pyautogui.click(1727, 555) #차트 내보내기 클릭
        time.sleep(0.2)
        pyautogui.click(1565, 555)  #데이터 내보내기 클릭
        pyautogui.click(1001, 384) 
        pyperclip.copy(f"{country}_Daily_by Model_{brand}_{pl}_{i}")
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'v')
        pyautogui.click(1160, 839) #extract

        
        pyautogui.moveTo(1914, 550)
        pyautogui.scroll(+700)
        pyautogui.moveTo(1913, 450)
        pyautogui.scroll(+500)
        pyautogui.moveTo(SCROLL_BAR)
        pyautogui.scroll(+500)
        time.sleep(1.5)

    except Exception as e:
        print(f"❌ 에러 발생: {e}") 


# 실행
start_time = time.time()
country = ["Brazil"]
brand_data = {
    "Apple": ["Apple iPhone Series", "Co.A Brand General"],
    "Generic": ["Foldable Generics", "Generic Others"],
    "Google" : ["Google Nexus", "Google Pixel Series"],
    "HONOR" : ["HONOR Brand General", "HONOR Magic Series","HONOR Number Series","HONOR Play","HONOR V Series",
                "HONOR View","HONOR Win","HONOR X Series"],
    "Huawei" : ["Huawei Ascend", "Huawei Brand General", "Huawei G Series", "Huawei Mate", 
                "Huawei Nexus", "Huawei Nova", "Huawei P Series", "Huawei Pura", "Huawei Y Series"],
    "Motorola" : ["Motorola Brand General", "Motorola Edge Series", "Motorola Moto C", "Motorola Moto E",
                  "Motorola Moto K", "Motorola Moto S","Motorola Moto X","Motorola Moto Z","Motorola Motoluxe",
                  "Motorola Nexus","Motorola One","Motorola Razr","Motorola V"],
    "OPPO" : ["OPPO Brand General","OPPO F Series", "OPPO Find Series","OPPO K Series","OPPO N Series",
              "OPPO Neo", "OPPO R Series", "OPPO RX Series", "OPPO Reno Series"],
    "OnePlus" : ["OnePlus Nord Series", "OnePlus One Series", "OnePlus Open Series", 
                 "OnePlus Brand General", "OnePlus Series",  "OnePlus X Series"],
    "realme" : ["realme", "realme Brand General","realme GT Series","realme Narzo Series", "realme Note Series", 
                "realme P Series", "realme Q Series", "realme U Series", "realme V Series", "realme X Series"],
    "Redmi" : [ "Redmi A Series", "Redmi Brand General", "Redmi Note Series",  "Redmi Series"],
    "Samsung" : ["Samsung Brand General", "Samsung Galaxy S",  "Samsung Galaxy Z"],
    "TCL" : ["TCL Brand General", "TCL PLEX", "TCL Trifold Series"],
    "Xiaomi" : ["Xiaomi Black Shark", "Xiaomi Brand General","Xiaomi Mi A",  "Xiaomi Mi MAX", "Xiaomi Mi MIX",
                 "Xiaomi Mi Note", "Xiaomi Mi Play",  "Xiaomi Mi Series",  "Xiaomi Pad"],
    "vivo" : ["vivo Apex", "vivo Brand General", "vivo Nex",  "vivo S series", "vivo T series", "vivo V Series", 
              "vivo Z Series", "vivo iQOO"]
}

brands = ["Motorola", "OPPO", "realme", "Samsung", "Samsung", "vivo", "vivo"]
pl_model_data = {
    "Motorola Moto G" : [
        "Motorola Moto G05","Motorola Moto G06","Motorola Moto G15","Motorola Moto G20","Motorola Moto G34 5G",
        "Motorola Moto G35 5G","Motorola Moto G4","Motorola Moto G4 Play","Motorola Moto G5","Motorola Moto G5 Plus",
        "Motorola Moto G54","Motorola Moto G55","Motorola Moto G56","Motorola Moto G57","Motorola Moto G5S",
        "Motorola Moto G5S Plus","Motorola Moto G6","Motorola Moto G6 Play","Motorola Moto G6 Plus","Motorola Moto G67",
        
        "Motorola Moto G7","Motorola Moto G7 Play","Motorola Moto G7 Plus", "Motorola Moto G7 Power","Motorola Moto G84", 
        "Motorola Moto G85", "Motorola Moto G86", "Motorola Moto G9", "Motorola Moto G96"
    ],
    "OPPO A Series" : [
        "OPPO A1","OPPO A11","OPPO A12","OPPO A15","OPPO A16",
        "OPPO A17","OPPO A18","OPPO A20","OPPO A22","OPPO A3",
        "OPPO A31","OPPO A32","OPPO A33","OPPO A37","OPPO A38",
        "OPPO A39","OPPO A40","OPPO A5","OPPO A52","OPPO A53",

        "OPPO A54","OPPO A57","OPPO A58","OPPO A6","OPPO A60",
        "OPPO A71","OPPO A72","OPPO A73","OPPO A74","OPPO A77",
        "OPPO A78","OPPO A79","OPPO A80","OPPO A83","OPO A9",
        "OPPO A91","OPPO A92","OPPO A93","OPPO A94","OPPO A95",

        "OPPO A98","OPPO AX7"
    ],
    "realme C Series" : [
        "realme C1","realme C100","realme C11","realme C12","realme C15",
        "realme C2","realme C20","realme C21","realme C25","realme C3",
        "realme C30","realme C33","realme C53","realme C55","realme C61",
        "realme C63","realme C65","realme C67","realme C71","realme C75",

        "realme C85"
    ],
    "Samsung Galaxy A" : [
        "Samsung Galaxy A01","Samsung Galaxy A02 Core","Samsung Galaxy A02s","Samsung Galaxy A03","Samsung Galaxy A03 Core",
        "Samsung Galaxy A03s","Samsung Galaxy A04","Samsung Galaxy A04e","Samsung Galaxy A04s","Samsung Galaxy A05",
        "Samsung Galaxy A05s","Samsung Galaxy A06","Samsung Galaxy A06s","Samsung Galaxy A07","Samsung Galaxy A10",
        "Samsung Galaxy A10e","Samsung Galaxy A10s","Samsung Galaxy A11","Samsung Galaxy A12","Samsung Galaxy A13",
        
        "Samsung Galaxy A14","Samsung Galaxy A15","Samsung Galaxy A16","Samsung Galaxy A17","Samsung Galaxy A20",
        "Samsung Galaxy A20e","Samsung Galaxy A20s","Samsung Galaxy A21","Samsung Galaxy A21s","Samsung Galaxy A22",
        "Samsung Galaxy A23","Samsung Galaxy A23 5G","Samsung Galaxy A24","Samsung Galaxy A25","Samsung Galaxy A25 5G",
        "Samsung Galaxy A26","Samsung Galaxy A30","Samsung Galaxy A30s","Samsung Galaxy A31","Samsung Galaxy A32",
        
        "Samsung Galaxy A33","Samsung Galaxy A34","Samsung Galaxy A35","Samsung Galaxy A36","Samsung Galaxy A37",
        "Samsung Galaxy A40","Samsung Galaxy A41","Samsung Galaxy A42","Samsung Galaxy A5","Samsung Galaxy A50",
        "Samsung Galaxy A50s","Samsung Galaxy A51","Samsung Galaxy A52","Samsung Galaxy A52 5G","Samsung Galaxy A52s 5G",
        "Samsung Galaxy A53","Samsung Galaxy A54","Samsung Galaxy A55","Samsung Galaxy A55 5G","Samsung Galaxy A56",
        
        "Samsung Galaxy A57","Samsung Galaxy A58","Samsung Galaxy A5s","Samsung Galaxy A6","Samsung Galaxy A6 Plus",
        "Samsung Galaxy A60","Samsung Galaxy A6s","Samsung Galaxy A70","Samsung Galaxy A70s","Samsung Galaxy A71",
        "Samsung Galaxy A72","Samsung Galaxy A73","Samsung Galaxy A8","Samsung Galaxy A8 Plus","Samsung Galaxy A8 Star",
        "Samsung Galaxy A80","Samsung Galaxy A80s","Samsung Galaxy A9","Samsung Galaxy A90"
    ],
    "Samsung Others" : [
        "Samsung Galaxy Ace","Samsung Galaxy Ace 2","Samsung Galaxy Ace 3","Samsung Galaxy Ace 4","Samsung Galaxy Ace Duos",
        "Samsung Galaxy Alpha","Samsung Galaxy C10","Samsung Galaxy C5","Samsung Galaxy C7","Samsung Galaxy C8",
        "Samsung Galaxy C9","Samsung Galaxy Core","Samsung Galaxy Core 2","Samsung Galaxy Core Plus","Samsung Galaxy Core Prime",
        "Samsung Galaxy Express","Samsung Galaxy Express 2","Samsung Galaxy Express 3","Samsung Galaxy F02s","Samsung Galaxy F04",
        
        "Samsung Galaxy F05","Samsung Galaxy F06","Samsung Galaxy F07","Samsung Galaxy F12","Samsung Galaxy F13",
        "Samsung Galaxy F14","Samsung Galaxy F14 5G","Samsung Galaxy F15 5G","Samsung Galaxy F16","Samsung Galaxy F17",
        "Samsung Galaxy F22","Samsung Galaxy F23","Samsung Galaxy F24","Samsung Galaxy F25","Samsung Galaxy F36",
        "Samsung Galaxy F41","Samsung Galaxy F42","Samsung Galaxy F54","Samsung Galaxy F55","Samsung Galaxy F56",
        
        "Samsung Galaxy F62","Samsung Galaxy Fame","Samsung Galaxy Fame Lite","Samsung Galaxy Fresh S7390","Samsung Galaxy Gio",
        "Samsung Galaxy Grand","Samsung Galaxy Grand 2","Samsung Galaxy Grand 2 Duos","Samsung Galaxy Grand Neo","Samsung Galaxy Grand Neo Plus",
        "Samsung Galaxy Grand Plus","Samsung Galaxy Grand Prime","Samsung Galaxy Grand Prime Plus","Samsung Galaxy Grand Prime Pro","Samsung Galaxy J1",
        "Samsung Galaxy J1 Ace","Samsung Galaxy J1 Mini","Samsung Galaxy J1 Mini Prime","Samsung Galaxy J2","Samsung Galaxy J2 Core",
        
        "Samsung Galaxy J2 Prime","Samsung Galaxy J2 Pro","Samsung Galaxy J3","Samsung Galaxy J3 Prime","Samsung Galaxy J3 Pro",
        "Samsung Galaxy J4","Samsung Galaxy J4 Core","Samsung Galaxy J4 Plus","Samsung Galaxy J5","Samsung Galaxy J5 Prime",
        "Samsung Galaxy J5 Pro","Samsung Galaxy J6","Samsung Galaxy J6 Plus","Samsung Galaxy J7","Samsung Galaxy J7 Core",
        "Samsung Galaxy J7 Neo","Samsung Galaxy J7 Plus","Samsung Galaxy J7 Prime","Samsung Galaxy J7 Pro","Samsung Galaxy J8",
        
        "Samsung Galaxy M01","Samsung Galaxy M01 Core","Samsung Galaxy M01s","Samsung Galaxy M02","Samsung Galaxy M02s",
        "Samsung Galaxy M06","Samsung Galaxy M10","Samsung Galaxy M10s","Samsung Galaxy M11","Samsung Galaxy M12",
        "Samsung Galaxy M13","Samsung Galaxy M14","Samsung Galaxy M14 5G","Samsung Galaxy M15","Samsung Galaxy M16",
        "Samsung Galaxy M17","Samsung Galaxy M20","Samsung Galaxy M21","Samsung Galaxy M30","Samsung Galaxy M30s",
        
        "Samsung Galaxy M31","Samsung Galaxy M31 Prime","Samsung Galaxy M31s","Samsung Galaxy M32","Samsung Galaxy M33",
        "Samsung Galaxy M34","Samsung Galaxy M35","Samsung Galaxy M36","Samsung Galaxy M42","Samsung Galaxy M51",
        "Samsung Galaxy M52","Samsung Galaxy M53","Samsung Galaxy M55","Samsung Galaxy M56","Samsung Galaxy Mega 2",
        "Samsung Galaxy Mega 5.8","Samsung Galaxy Mega 6.3","Samsung Galaxy Mini","Samsung Galaxy Mini 2","Samsung Galaxy Nexus",
        
        "Samsung Galaxy Note","Samsung Galaxy Note 10","Samsung Galaxy Note 2","Samsung Galaxy Note 20","Samsung Galaxy Note 3",
        "Samsung Galaxy Note 4","Samsung Galaxy Note 5","Samsung Galaxy Note 7","Samsung Galaxy Note 8","Samsung Galaxy Note 9",
        "Samsung Galaxy Note Edge","Samsung Galaxy Trend","Samsung Galaxy Trend 2 Lite","Samsung Galaxy Trend Lite","Sasung Galaxy Trend Plus",
        "Samsung Galaxy Win Duos","Samsung Galaxy Xcover","Samsung Galaxy Xcover 2","Samsung Galaxy Xcover 3","Samsung Galaxy Xcover 4",
        
        "Samsung Galaxy Y","Samsung Galaxy Y Pro","Samsung Galaxy Young","Samsung Galaxy Young 2","Samsung Z1",
        "Samsung Z2","Samsung Z3","Samsung Z4","Samsung Z5"
    ],
    "vivo X Series" : [
        "vivo X Fold3","vivo X Fold5","vivo X100","vivo X20","vivo X200",
        "vivo X21","vivo X23","vivo X25","vivo X27","vivo X3",
        "vivo X30","vivo X300","vivo X5","vivo X50","vivo X6",
        "vivo X60","vivo X7","vivo X70","vivo X80","vivo X9",
        
        "vivo X90"
    ],
    "vivo Y Series" : [
        "vivo Y02","vivo Y03","vivo Y04","vivo Y091","vivo Y100",
        "vivo Y12","vivo Y15","vivo Y16","vivo Y17","vivo Y18",
        "vivo Y19","vivo Y20","vivo Y200","vivo Y21","vivo Y22",
        "vivo Y27","vivo Y28","vivo Y29","vivo Y30","vivo Y300",

        "vivo Y31","vivo Y33","vivo Y35","vivo Y36","vivo Y38",
        "vivo Y39","vivo Y400","vivo Y50","vivo Y51","vivo Y53",
        "vivo Y55","vivo Y58","vivo Y65","vivo Y66","vivo Y69",
        "vivo Y70","vivo Y71","vivo Y72","vivo Y76","vivo Y81",

        "vivo Y83","vivo Y85","vivo Y93","vivo Y95"
    ]
}

# filter("COUNTRY",country)
# filter("BRAND",brand)
# filter("PL",pl[0])


i=0
for pl, model in pl_model_data.items():
    if "Others" not in pl:
        i += 1
        continue 

    filter("PL", pl) 
    j=0
    for chunk in get_chunks(model, 20):
    # 여기서 chunk는 20개짜리 리스트가 됩니다.
        j += 1
        filter_model(chunk)
        by_model(country, brands[i], pl, j)
    i += 1
    pyautogui.click(filter_coords["MODEL"]["BUTTON"])
    pyautogui.click(filter_coords["MODEL"]["UNFILTER_BUTTON"])
    unfilter()
    pyautogui.click(819, 331)
    pyautogui.click(762, 318)
    pyautogui.click(773, 284)

# for c in country:
#     filter("COUNTRY", c) 
#     by_model(c, "realme", "realme X Series")

# by_brand(country)   
# for br, items in brand_data.items():
#     if br not in ["Google", "HONOR", "OnePlus"]:
#         continue 
#     filter("BRAND", br) 
#     by_pl(country, br)

#     for pl_item in items:
#         filter("PL", pl_item) 
#         by_model(country, br, pl_item)
    
#     unfilter()

end_time = time.time()
print(f"⏱️ 작업 소요 시간: {(end_time - start_time)/60:.2f}분")