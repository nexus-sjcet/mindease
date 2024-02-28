/*
  Warnings:

  - You are about to drop the `Scores` table. If the table is not empty, all the data it contains will be lost.

*/
-- DropForeignKey
ALTER TABLE "Scores" DROP CONSTRAINT "Scores_userPhone_fkey";

-- DropTable
DROP TABLE "Scores";

-- CreateTable
CREATE TABLE "Score" (
    "id" TEXT NOT NULL DEFAULT (gen_random_uuid())::text,
    "createdAt" TIMESTAMP(0) NOT NULL DEFAULT CURRENT_TIMESTAMP,
    "Extroversion" DOUBLE PRECISION NOT NULL,
    "Agreeableness" DOUBLE PRECISION NOT NULL,
    "Conscientiousness" DOUBLE PRECISION NOT NULL,
    "Neuroticism" DOUBLE PRECISION NOT NULL,
    "Openness" DOUBLE PRECISION NOT NULL,
    "userPhone" TEXT,

    CONSTRAINT "Score_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "Score_id_key" ON "Score"("id");

-- AddForeignKey
ALTER TABLE "Score" ADD CONSTRAINT "Score_userPhone_fkey" FOREIGN KEY ("userPhone") REFERENCES "User"("phone") ON DELETE SET NULL ON UPDATE CASCADE;
