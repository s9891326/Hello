from hello_pattern.template_pattern.story_video import StoryVideo
from hello_pattern.template_pattern.tutorial_video import TutorialVideo
from hello_pattern.template_pattern.unbox_video import UnboxVideo


class Program:
    
    # first design
    # 有很多共同點，寫成樣板供大家使用
    def make_unbox_video(self):
        return '選擇開箱項目、拍攝、剪輯出個人開箱的風格、上傳影片'
    
    def make_tutorial_video(self):
        return '設計教學內容、拍攝、剪輯出個人教學的風格、上傳影片'
    
    def make_story_video(self):
        return '選擇故事主題、拍攝、剪輯出個人說故事的風格、上傳影片'
    
    # use template pattern > 去寫成樣板
    def make_unbox_video_2(self):
        return UnboxVideo().make()
    
    def make_tutorial_video_2(self):
        return TutorialVideo().make()
    
    def make_story_video_2(self):
        return StoryVideo().make()


if __name__ == '__main__':
    program = Program()
    # print(program.make_unbox_video())
    # print(program.make_tutorial_video())
    # print(program.make_story_video())

    print(program.make_unbox_video_2())
    print(program.make_tutorial_video_2())
    print(program.make_story_video_2())
