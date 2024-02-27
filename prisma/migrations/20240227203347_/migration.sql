/*
  Warnings:

  - You are about to alter the column `Extroversion` on the `AnalysisData` table. The data in that column could be lost. The data in that column will be cast from `Decimal(65,30)` to `DoublePrecision`.
  - You are about to alter the column `Agreeableness` on the `AnalysisData` table. The data in that column could be lost. The data in that column will be cast from `Decimal(65,30)` to `DoublePrecision`.
  - You are about to alter the column `Conscientiousness` on the `AnalysisData` table. The data in that column could be lost. The data in that column will be cast from `Decimal(65,30)` to `DoublePrecision`.
  - You are about to alter the column `Neuroticism` on the `AnalysisData` table. The data in that column could be lost. The data in that column will be cast from `Decimal(65,30)` to `DoublePrecision`.
  - You are about to alter the column `Openness` on the `AnalysisData` table. The data in that column could be lost. The data in that column will be cast from `Decimal(65,30)` to `DoublePrecision`.

*/
-- AlterTable
ALTER TABLE "AnalysisData" ALTER COLUMN "Extroversion" SET DATA TYPE DOUBLE PRECISION,
ALTER COLUMN "Agreeableness" SET DATA TYPE DOUBLE PRECISION,
ALTER COLUMN "Conscientiousness" SET DATA TYPE DOUBLE PRECISION,
ALTER COLUMN "Neuroticism" SET DATA TYPE DOUBLE PRECISION,
ALTER COLUMN "Openness" SET DATA TYPE DOUBLE PRECISION;
