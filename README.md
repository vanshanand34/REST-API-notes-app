This project is a Django-based Notes App which contains different API endpoints developed using DRF(Django Rest Framework)
It consists of API Endpoints for login  , registering new users , logout and Performing CRUD operations on the notes.

LOGIN:

The login is implemented using token based authentication ( the built in Token object from django.contrib.authtoken ) .
For Implementaion of notes , a note object along with its corresponding NoteSerializer is created.
Serializers are used for conversion of python based dictionaries into Json format to transfer data through request-response cycles.

NOTE OBJECT:

The Note object consists of fields content , title , user( storing the user object who created the note) , timestamp ( time when the note is created ) and allowed_users(charField).
The allowed_users field is the field through which notes can be shared between different users.
A user who creates a note can specify the emails of the users which can access that particular note ( only read ) in this allowed_users field of the note object.
The user field of a note is assigned the user object who creates it at the time of creation.
Creator of a note need to specify only the title , content and allowed_users(if any).

PERMISSIONS:

A user can only view a note or access a note only  after login.
Also only the notes in which the user's email is specified in the allowed_users field or the user is the creator of note can access it.
Any user can delete or update only notes created by him/her.

ACCESS:

As it is based on a token based authentication , on login (or register) a token is returned which can be used for successive requests as they are mainly API Endpoints.
