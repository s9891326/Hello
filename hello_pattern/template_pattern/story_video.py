from hello_pattern.template_pattern.basic_video import BasicVideo


class StoryVideo(BasicVideo):
    
    def editing(self):
        return '剪輯出個人說故事的風格'

    def generate_ideas(self):
        return "選擇故事主題"

