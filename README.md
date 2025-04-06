
# 🖼️ AWS Lambda Image Compressor with Pillow (Python 3.11)

This Lambda function automatically compresses JPEG images uploaded to an S3 bucket using the Pillow library. It works with a custom Lambda Layer compiled for Python 3.11.

---

## 🔧 Features

- Automatically compresses JPEG images upon upload to an S3 bucket
- Uses Pillow for image processing
- Optimized for AWS Lambda (Python 3.11)
- Includes a Lambda Layer with pre-built Pillow package

---

## 📁 Project Structure

```
lambda/
│
├── lambda_function.py        # Main Lambda handler
├── pillow_layer.zip          # Lambda Layer with Pillow (Python 3.11)
```

---

## 🔑 IAM Role Configuration

Your Lambda function must be assigned an IAM Role with the following permissions:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:s3:::<source-bucket>/*",
        "arn:aws:s3:::<destination-bucket>/*"
      ]
    }
  ]
}
```

> ✅ You can also attach the managed policy `AmazonS3FullAccess` during testing.

---

## 🧠 Lambda Configuration

- **Runtime:** Python 3.11
- **Memory:** 256 MB (recommended for larger images)
- **Timeout:** 10 seconds or more (3s might timeout for large images)
- **Handler:** `lambda_function.lambda_handler`
- **Layer:** Upload `pillow_layer.zip` as a Lambda Layer and attach to your function

---

## 🚀 Deployment Steps

1. **Create Lambda Layer:**

   - Upload pillow_layer.zip as a Lambda Layer file or you can use the below ARN.
   - please ensure to select runtime as Python 3.11
     arn:aws:lambda:ap-south-1:975050024946:layer:new_pillow_layer_avi:1

2. **Upload Your Lambda Function**

   - Copy paste the `lambda_function.py` in the code section, ensure to put destination bucket name in the code.
   - Test and see if it does not result in any library error.
   - Launch your Function
  
## Screenshots

 - Source Bucket
   
<img width="756" alt="image" src="https://github.com/user-attachments/assets/8719be2c-c7f9-4698-a514-664f826799b4" />

- Destination Bucket

  <img width="709" alt="image" src="https://github.com/user-attachments/assets/a3a6afaf-fc9e-4d4d-b967-3488ccaaec6c" />



## 📝 Notes

- Ensure the S3 event trigger is properly configured.
- Pillow version must match Python runtime.
- Always test with smaller images first before scaling up.

---

## 🙌 Done!

