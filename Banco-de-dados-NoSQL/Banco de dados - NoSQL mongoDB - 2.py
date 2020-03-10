#!/usr/bin/env python
# coding: utf-8

# # Banco de dados MongoDB
# ## NoSQL

# Chamar o banco de dados no cmd
# mongod

# In[1]:


import pymongo


# In[2]:


client_con = pymongo.MongoClient()


# In[3]:


client_con.database_names()


# In[4]:


db = client_con.cadastrodb


# In[5]:


db.collection_names()


# In[6]:


db.collection_names()


# In[7]:


db.mycollection.insert_one({
   'titulo': 'MongoDB', 
   'descricao': 'NoSQL',
   'by': 'GHR-System',
   'url': 'http://www.ghrsystem.com.br',
   'tags': ['mongodb', 'database', 'NoSQL'],
   'likes': 100
})


# In[8]:


db.mycollection.find_one()


# In[9]:


doc1 = {"Nome":"ghrsystem","twitter":"@ghrsystem"}


# In[10]:


db.mycollection.insert_one(doc1)


# In[11]:


doc2 = {"Site":"http://www.ghrsystem.com.br",
        "facebook":"facebook.com/ghrsystem"}


# In[12]:


db.mycollection.insert_one(doc2)


# In[13]:


for rec in db.mycollection.find():
    print(rec)


# In[14]:


col = db['mycollection']


# In[15]:


col.count()


# In[16]:


redoc = col.find_one()
redoc

