#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import qrcode

img = qrcode.make("Hello! My name is Mursal Asadulla. You can contact me at maryasadulla3@gmail.com")
img.save("mycode.png")

