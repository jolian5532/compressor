import os
from bs4 import BeautifulSoup
from jsmin import jsmin
from csscompressor import compress
import htmlmin

# js, css, html
class ffile:
    html_path = None
    def __init__(self,config):
        self.config = config  

    def minjs(self,javascript):
        # TODO: code obfuscation
        return jsmin(javascript)
    def mincss(self,content):
        return compress(content)
    def css(self, csspath):
        with open(csspath, 'r') as file:
            csscontent = file.read()
        with open(csspath, 'w') as file:
            file.write(self.mincss(csscontent))
    def js(self, jspath):
        with open(jspath, 'r') as file:
            jscotent = file.read()
        with open(jspath, 'w') as file:
            file.write(self.minjs(jscotent))

    def html(self, htmlpath):
        if htmlpath == None:
            return None
        if self.config["convert"]:
            with open(htmlpath, 'r') as file:
                html_content = file.read()
            soup = BeautifulSoup(html_content, 'html.parser')
            img_tags = soup.find_all('img')
            for img_tag in img_tags:
                src_attr = img_tag.get('src')
                if src_attr:
                    file_name, extension = os.path.splitext(src_attr)
                    new_extension = self.config["convert"].get(extension[1:].upper()) 
                    if new_extension:
                        if  os.path.basename(img_tag['src']) in self.config['imgs']:
                            # TODO: maybe add picture tag and srcset attribute!
                            img_tag['src'] = file_name + '.' + new_extension.lower()
            
            script_tags = soup.find_all('script')
            for script_tag in script_tags:
                if script_tag.string:
                    compressed_content = self.minjs(script_tag.string)
                    script_tag.string = compressed_content
            style_tags = soup.find_all('style')
            for style_tag in style_tags:
                style_tag.string = self.mincss(style_tag.string)
            elements_with_inline_css = soup.find_all(attrs={'style': True})
            for element in elements_with_inline_css:
                inline_css = element['style']
                # TODO: change converted image links
                element['style'] = self.mincss(inline_css)
        with open(htmlpath, 'w') as file:
            file.write(htmlmin.minify(soup.prettify()))
        return htmlpath
        
