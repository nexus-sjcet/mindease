/*
  Warnings:

  - You are about to drop the column `userPhone` on the `Score` table. All the data in the column will be lost.

*/
-- DropForeignKey
ALTER TABLE "Score" DROP CONSTRAINT "Score_userPhone_fkey";

-- AlterTable
ALTER TABLE "Score" DROP COLUMN "userPhone",
ADD COLUMN     "userId" TEXT;

-- AddForeignKey
ALTER TABLE "Score" ADD CONSTRAINT "Score_userId_fkey" FOREIGN KEY ("userId") REFERENCES "User"("id") ON DELETE SET NULL ON UPDATE CASCADE;
