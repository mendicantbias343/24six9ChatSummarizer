from linkpreview import link_preview



preview = link_preview("https://www.linkedin.com/feed/update/urn:li:activity:7096489876254015488")
print("title:", preview.title)
print("description:", preview.description)
print("image:", preview.image)
print("force_title:", preview.force_title)
print("absolute_image:", preview.absolute_image)
print("site_name:", preview.site_name)