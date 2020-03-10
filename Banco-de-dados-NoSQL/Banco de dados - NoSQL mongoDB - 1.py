#!/usr/bin/env python
# coding: utf-8

# In[1]:


from pymongo import MongoClient


# In[2]:


conn = MongoClient('localhost', 27017)


# In[3]:


db = conn.cadastrodb


# In[4]:


collection = db.cadastrodb


# In[5]:


import datetime


# In[6]:


post1 = {"codigo": "ID-202045",
        "formação": "curso em python",
        "cursos": ["R", "Python", "C#"],
        "data_curso": datetime.datetime.utcnow()}


# In[7]:


collection = db.posts


# In[8]:


post_id = collection.insert_one(post1)


# In[9]:


post_id.inserted_id


# In[10]:


post_id


# In[11]:


post2 = {"codigo": "ID-8975462",
        "formação": "Cientista de dados",
        "curso": ["Python", "R", "C#"],
        "data_cadastro": datetime.datetime.utcnow()}


# In[12]:


collection = db.posts


# In[13]:


post_id = collection.insert_one(post2).inserted_id


# In[14]:


post_id


# In[15]:


collection.find_one({"formação": "Cientista de dados"})


# In[16]:


for post in collection.find():
    print(post)


# In[17]:


db.name


# In[18]:


db.collection_names()


# In[ ]:




