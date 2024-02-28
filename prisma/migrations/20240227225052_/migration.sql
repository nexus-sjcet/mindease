/*
  Warnings:

  - You are about to drop the column `userId` on the `Score` table. All the data in the column will be lost.

*/
-- DropForeignKey
ALTER TABLE "Score" DROP CONSTRAINT "Score_userId_fkey";

-- AlterTable
ALTER TABLE "Score" DROP COLUMN "userId",
ADD COLUMN     "userPhone" TEXT;

-- AddForeignKey
ALTER TABLE "Score" ADD CONSTRAINT "Score_userPhone_fkey" FOREIGN KEY ("userPhone") REFERENCES "User"("phone") ON DELETE SET NULL ON UPDATE CASCADE;
