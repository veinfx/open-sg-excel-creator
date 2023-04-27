import shotgun_api3

SERVER_PATH = "https://url.shotgrid.autodesk.com"
SCRIPT_NAME = "script name"
SCRIPT_KEY = "script key"

sg = shotgun_api3.Shotgun(SERVER_PATH,
                          script_name=SCRIPT_NAME, api_key=SCRIPT_KEY)


class ShotgunApi:
    """
    로컬에 있는 파일을 샷그리드의 Asset 에 upload 하기위해 shotgun_api3 를 맵핑한 api 이다.
    """
    def __init__(self):
        pass

    def get_user_data_info(self, entity_type, ids):
        """핸들러의 해당 엔티티의 id(들)을 전달 받아서
        찾고싶은 필드와 필터를 설정하여 sg.find 로 asset,shot info 데이터를 리턴한다.
        """
        assets = None
        shots = None
        fields = ["code", "sg_status_list"]
        filters = [['id', 'in', ids]]

        if entity_type == "Asset":
            fields.append("sg_asset_type")
            assets = sg.find(entity_type, filters, fields)

        elif entity_type == "Shot":
            fields.append("sg_sequence")
            shots = sg.find(entity_type, filters, fields)

        return assets, shots