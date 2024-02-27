-- CreateTable
CREATE TABLE "User" (
    "id" TEXT NOT NULL DEFAULT (gen_random_uuid())::text,
    "name" TEXT NOT NULL,
    "phone" TEXT NOT NULL,
    "createdAt" TIMESTAMP(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT "User_pkey" PRIMARY KEY ("id")
);

-- CreateTable
CREATE TABLE "AnalysisData" (
    "id" TEXT NOT NULL DEFAULT (gen_random_uuid())::text,
    "createdAt" TIMESTAMP(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "Extroversion" DECIMAL(65,30) NOT NULL,
    "Agreeableness" DECIMAL(65,30) NOT NULL,
    "Conscientiousness" DECIMAL(65,30) NOT NULL,
    "Neuroticism" DECIMAL(65,30) NOT NULL,
    "Openness" DECIMAL(65,30) NOT NULL,
    "userId" TEXT,

    CONSTRAINT "AnalysisData_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "User_id_key" ON "User"("id");

-- CreateIndex
CREATE UNIQUE INDEX "User_phone_key" ON "User"("phone");

-- CreateIndex
CREATE UNIQUE INDEX "AnalysisData_id_key" ON "AnalysisData"("id");

-- AddForeignKey
ALTER TABLE "AnalysisData" ADD CONSTRAINT "AnalysisData_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE SET NULL ON UPDATE CASCADE;
