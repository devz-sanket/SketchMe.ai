from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse, JSONResponse
from io import BytesIO
from utils import transform_image

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/transform")
async def transform(image: UploadFile = File(...), mode: str = Form(...)):
    try:
        contents = await image.read()
        result_image = transform_image(contents, mode)

        buffer = BytesIO()
        result_image.save(buffer, format="PNG")
        buffer.seek(0)

        return StreamingResponse(buffer, media_type="image/png")

    except Exception as e:
        import traceback
        print("🔥 ERROR OCCURRED:")
        traceback.print_exc()
        return JSONResponse(content={"error": str(e)}, status_code=500)
