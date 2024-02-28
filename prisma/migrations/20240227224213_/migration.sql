/*
  Warnings:

  - You are about to drop the column `Agreeableness` on the `Score` table. All the data in the column will be lost.
  - You are about to drop the column `Conscientiousness` on the `Score` table. All the data in the column will be lost.
  - You are about to drop the column `Extroversion` on the `Score` table. All the data in the column will be lost.
  - You are about to drop the column `Neuroticism` on the `Score` table. All the data in the column will be lost.
  - You are about to drop the column `Openness` on the `Score` table. All the data in the column will be lost.
  - Added the required column `agreeableness` to the `Score` table without a default value. This is not possible if the table is not empty.
  - Added the required column `conscientiousness` to the `Score` table without a default value. This is not possible if the table is not empty.
  - Added the required column `extroversion` to the `Score` table without a default value. This is not possible if the table is not empty.
  - Added the required column `neuroticism` to the `Score` table without a default value. This is not possible if the table is not empty.
  - Added the required column `openness` to the `Score` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "Score" DROP COLUMN "Agreeableness",
DROP COLUMN "Conscientiousness",
DROP COLUMN "Extroversion",
DROP COLUMN "Neuroticism",
DROP COLUMN "Openness",
ADD COLUMN     "agreeableness" DOUBLE PRECISION NOT NULL,
ADD COLUMN     "conscientiousness" DOUBLE PRECISION NOT NULL,
ADD COLUMN     "extroversion" DOUBLE PRECISION NOT NULL,
ADD COLUMN     "neuroticism" DOUBLE PRECISION NOT NULL,
ADD COLUMN     "openness" DOUBLE PRECISION NOT NULL;
