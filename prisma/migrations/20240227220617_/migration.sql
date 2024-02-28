/*
  Warnings:

  - You are about to drop the `AnalysisData` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "AnalysisData" DROP CONSTRAINT "AnalysisData_userId_fkey";

-- DropTable
DROP TABLE "AnalysisData";

-- CreateTable
CREATE TABLE "Scores" (
    "id" TEXT NOT NULL DEFAULT (gen_random_uuid())::text,
    "createdAt" TIMESTAMP(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "Extroversion" DOUBLE PRECISION NOT NULL,
    "Agreeableness" DOUBLE PRECISION NOT NULL,
    "Conscientiousness" DOUBLE PRECISION NOT NULL,
    "Neuroticism" DOUBLE PRECISION NOT NULL,
    "Openness" DOUBLE PRECISION NOT NULL,
    "userPhone" TEXT,

    CONSTRAINT "Scores_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Scores_id_key" ON "Scores"("id");

-- AddForeignKey
ALTER TABLE "Scores" ADD CONSTRAINT "Scores_userPhone_fkey" FOREIGN KEY ("userPhone") REFERENCES "User"("phone") ON DELETE SET NULL ON UPDATE CASCADE;
