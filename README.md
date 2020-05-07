# The Mox and Louise QR Code Verification System!

This is where the moxandlouise.com QR code system is kept. 

It is a work in progress and is being updated daily as part of a rebuilding effort. 

There are two components to this project. First is the Python based PyQT5 GUI application used by the Client (Mox&Louise) to generate new QR codes, upload images, and update the backend database.

Second, the AWS backend and verification website built with the Vue.js framework. The AWS Backend uses S3 for hosting the static single page application (SPA), and DynamoDB for the NoSQL database. This SPA connects via an API Gateway HTTP API to a Lambda Backend function which verifies the doll based on an ID. The SPA then fetches the images and descriptors for the doll.

The QR codes encode a URL that links the user to the verification website. eg "https://verify.moxandlouise.com/#123456"
where 123456 is a sample ID, in practice they are 8 character random UUID generated values which are looked up in the database.
