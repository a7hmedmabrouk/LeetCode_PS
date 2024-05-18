class Solution {
public:
    int distributeCoins(TreeNode* root) {
        int moves = 0;
        postOrder(root, moves);
        return moves;
    }
private:
    int postOrder(TreeNode* node, int& moves) {
        if (!node) return 0;
        int leftBalance = postOrder(node->left, moves);
        int rightBalance = postOrder(node->right, moves);
        int balance = node->val + leftBalance + rightBalance - 1;
        moves += abs(balance);
        return balance;
    }
};