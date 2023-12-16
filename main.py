from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_text_post(self, text_post: "TextPost"):
        pass

    @abstractmethod
    def visit_image_post(self, image_post: "ImagePost"):
        pass

    @abstractmethod
    def visit_video_post(self, video_post: "VideoPost"):
        pass

class PrintExportVisitor(Visitor):
    def visit_text_post(self, text_post: "TextPost"):
        print(
            f"Text Post with ID={text_post.get_id()} "
            f"has been read {text_post.get_display_count()} times! "
            f"Text: {text_post.get_text()}"
        )

    def visit_image_post(self, image_post: "ImagePost"):
        print(
            f"Image Post with ID={image_post.get_id()} "
            f"has been seen {image_post.get_display_count()} times! "
            f"Image: {image_post.get_image()}"
        )

    def visit_video_post(self, video_post: "VideoPost"):
        print(
            f"Video Post with ID={video_post.get_id()} "
            f"has been watched {video_post.get_display_count()} times! "
            f"Video: {video_post.get_video()}"
        )

class Post(ABC):
    ID = 0


    def __init__(self):
        self.__id = Post.ID + 1
        self.__display_count = 0
        Post.ID += 1

    def get_id(self):
        return self.__id

    def get_display_count(self):
        return self.__display_count

    def display(self):
        self.__display_count += 1     


    @abstractmethod
    def accept(self, visitor:Visitor):
        pass

class TextPost(Post):
    def __init__(self, text, author):
        super().__init__()
        self.__text = text
        self.__author = author

    def get_text(self):
        return self.__text
    
    def display(self):
        print(f"Displaying TextPost : Text: {self.__text}")
        super().display()

    def accept(self, visitor: Visitor):
        visitor.visit_text_post(self)


class ImagePost(Post):
    def __init__(self, image, author):
        super().__init__()
        self.__image = image
        self.__author = author

    def get_image(self):
        return self.__image

    def display(self):
        print(f"Displaying ImagePost : Image: {self.__image}")
        super().display()

    def accept(self, visitor: Visitor):
        visitor.visit_image_post(self)


class VideoPost(Post):
    def __init__(self, video, author):
        super().__init__()
        self.__video = video
        self.__author = author

    def get_video(self):
        return self.__video

    def display(self):
        print(f"Displaying VideoPost : Video: {self.__video}")
        super().display()

    def accept(self, visitor: Visitor):
        visitor.visit_video_post(self)


def main():
    posts = [
        TextPost(text="Post 1", author="Uncle Bob"),
        ImagePost(image="/src/image/img1.png", author="Uncle Bob"),
        VideoPost(video="/src/video/vid1.png", author="John Doe"),
    ]
    posts[0].display()
    posts[1].display()
    posts[2].display()

    visitor = PrintExportVisitor()
    for post in posts:
        post.accept(visitor)

main()