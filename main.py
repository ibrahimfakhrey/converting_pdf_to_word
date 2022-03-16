
import convertapi
import os
import tempfile

convertapi.api_secret = 'YXIEyhvlCn9Pf24A'# your api secret

# Example of saving Word docx to PDF and to PNG
# https://www.convertapi.com/docx-to-pdf
# https://www.convertapi.com/docx-to-png

# Use upload IO wrapper to upload file only once to the API
upload_io = convertapi.UploadIO(open('/Users/Admin/Desktop/paper work/Quarter objectifs g10.docx', 'rb'))

saved_files = convertapi.convert('pdf', { 'File': upload_io }).save_files(tempfile.gettempdir())

print("The PDF saved to %s" % saved_files)

# Reuse the same uploaded file

saved_files = convertapi.convert('png', { 'File': upload_io }).save_files(tempfile.gettempdir())


print("The PNG saved to %s" % saved_files)